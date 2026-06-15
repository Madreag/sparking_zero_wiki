using System.Collections.Concurrent;
using CUE4Parse.Encryption.Aes;
using CUE4Parse.FileProvider;
using CUE4Parse.MappingsProvider;
using CUE4Parse.UE4.Localization;
using CUE4Parse.UE4.Objects.Core.Misc;
using CUE4Parse.UE4.Readers;
using CUE4Parse.UE4.Versions;
using Newtonsoft.Json;

const string PaksDir = @"D:\SteamLibrary\steamapps\common\DRAGON BALL Sparking! ZERO\SparkingZERO\Content\Paks";
const string UsmapPath = @"C:\vaults\sparking_zero\tools\Mappings_fresh.usmap";
const string AesKey = "0xb2407c45ea7c528738a94c0a25ea8f419de4377628eb30c0ae6a80dd9a9f3ef0";
const string OutDir = @"C:\vaults\sparking_zero\data-mined\raw";
const string Root = "SparkingZERO/Content/SS/MasterDataAsset/";

var oodlePath = Path.Combine(@"C:\vaults\sparking_zero\tools", "oo2core_9_win64.dll");
if (!File.Exists(oodlePath))
{
    try { await CUE4Parse.Compression.OodleHelper.DownloadOodleDllFromOodleUEAsync(new HttpClient(), oodlePath); }
    catch (Exception e) { Console.WriteLine($"OodleUE download failed: {e.Message}"); }
}
if (!File.Exists(oodlePath))
{
    Console.WriteLine("Falling back to XV2 oo2core_6 dll");
    File.Copy(@"D:\SteamLibrary\steamapps\common\DB Xenoverse 2\bin\oo2core_6_win64.dll", oodlePath);
}
CUE4Parse.Compression.OodleHelper.Initialize(oodlePath);
Console.WriteLine($"Oodle initialized: {oodlePath} ({new FileInfo(oodlePath).Length} bytes)");

var provider = new DefaultFileProvider(PaksDir, SearchOption.AllDirectories, new VersionContainer(EGame.GAME_UE5_1));
provider.MappingsContainer = new FileUsmapTypeMappingsProvider(UsmapPath);
provider.Initialize();
provider.SubmitKey(new FGuid(), new FAesKey(AesKey));
Console.WriteLine($"Mounted. Total files: {provider.Files.Count}");

var settings = new JsonSerializerSettings { Formatting = Formatting.Indented };
var failures = new ConcurrentBag<string>();

// Folders merged into a single JSON each
string[] simpleFolders = [
    "CharacterData", "AiCharacterData", "Numeric", "BlastSkill", "BlastForte", "BlastUltimate",
    "FormChange", "BuffForm", "DamageReactionData", "HitStopData", "HitBackMovement",
    "ArmorData", "ArmorBreakLevelData", "ArmorLevel", "Charge", "ZBurstDash", "DragonDash",
    "RevengeDash", "DashUpDown", "Warp", "Movement", "AttackHoming", "DragonHoming",
    "EnergyBulletDirectionData", "RankMatchRank", "Tournament", "DownLoadContents",
    "WishComeTrue", "ShopBaseItem", "ShopSalesItem", "ShopFloor", "StockItem", "MythicalOrbData",
    "MissionTrophyData", "MissionSortFilterData", "CharacterFilter", "EditParts",
    "ReplaceCharacterItem", "BattleTraining", "DramaticBattle", "DramaticBattleTips",
    "Battlemode010", "Battlemode010Tips", "ModeHUN", "ModeNSR", "Search", "PlayerMatch",
    "Ranking", "Announce", "Notification", "Terms", "OperationGuide", "Action",
    "ActionTranslation", "ReplaceTransitionAction", "Gallery", "RewardLottery", "PlayerCard"
];

// Folders grouped into one JSON per first-level subkey (avoids giant single files)
string[] groupedFolders = ["Combatives", "Buff", "Combination", "BulletSetting", "MissionData", "Reward", "CharacterItem", "DragonAdventureIF"];

object?[] LoadExports(string path)
{
    var pkg = provider.LoadPackage(path);
    return pkg.GetExports().Cast<object?>().ToArray();
}

void ExportMerged(string folder)
{
    var prefix = Root + folder + "/";
    var files = provider.Files.Keys.Where(p => p.StartsWith(prefix, StringComparison.OrdinalIgnoreCase) && p.EndsWith(".uasset")).ToList();
    if (files.Count == 0) { Console.WriteLine($"!! no files for {folder}"); return; }
    var dict = new ConcurrentDictionary<string, object?>();
    Parallel.ForEach(files, new ParallelOptions { MaxDegreeOfParallelism = 8 }, path =>
    {
        var name = Path.GetFileNameWithoutExtension(path);
        try { dict[name] = LoadExports(path); }
        catch (Exception e) { failures.Add($"{path}: {e.Message}"); }
    });
    var outPath = Path.Combine(OutDir, "masterdata", folder + ".json");
    Directory.CreateDirectory(Path.GetDirectoryName(outPath)!);
    File.WriteAllText(outPath, JsonConvert.SerializeObject(dict.OrderBy(kv => kv.Key, StringComparer.Ordinal).ToDictionary(kv => kv.Key, kv => kv.Value), settings));
    Console.WriteLine($"{folder}: {dict.Count}/{files.Count} -> {outPath}");
}

void ExportGrouped(string folder)
{
    var prefix = Root + folder + "/";
    var files = provider.Files.Keys.Where(p => p.StartsWith(prefix, StringComparison.OrdinalIgnoreCase) && p.EndsWith(".uasset")).ToList();
    if (files.Count == 0) { Console.WriteLine($"!! no files for {folder}"); return; }
    var groups = files.GroupBy(p =>
    {
        var rel = p.Substring(prefix.Length);
        var idx = rel.IndexOf('/');
        return idx < 0 ? "_root" : rel[..idx];
    });
    foreach (var g in groups)
    {
        var dict = new ConcurrentDictionary<string, object?>();
        Parallel.ForEach(g, new ParallelOptions { MaxDegreeOfParallelism = 8 }, path =>
        {
            var name = Path.GetFileNameWithoutExtension(path);
            try { dict[name] = LoadExports(path); }
            catch (Exception e) { failures.Add($"{path}: {e.Message}"); }
        });
        var outPath = Path.Combine(OutDir, "masterdata", folder, g.Key + ".json");
        Directory.CreateDirectory(Path.GetDirectoryName(outPath)!);
        File.WriteAllText(outPath, JsonConvert.SerializeObject(dict.OrderBy(kv => kv.Key, StringComparer.Ordinal).ToDictionary(kv => kv.Key, kv => kv.Value), settings));
    }
    Console.WriteLine($"{folder}: {files.Count} files in {groups.Count()} groups");
}

// 1) String tables
{
    var stFiles = provider.Files.Keys.Where(p => p.StartsWith("SparkingZERO/Content/SS/StringTables/", StringComparison.OrdinalIgnoreCase) && p.EndsWith(".uasset")).ToList();
    var dict = new ConcurrentDictionary<string, object?>();
    Parallel.ForEach(stFiles, path =>
    {
        var name = Path.GetFileNameWithoutExtension(path);
        try { dict[name] = LoadExports(path); }
        catch (Exception e) { failures.Add($"{path}: {e.Message}"); }
    });
    Directory.CreateDirectory(OutDir);
    File.WriteAllText(Path.Combine(OutDir, "stringtables.json"), JsonConvert.SerializeObject(dict.OrderBy(kv => kv.Key, StringComparer.Ordinal).ToDictionary(kv => kv.Key, kv => kv.Value), settings));
    Console.WriteLine($"StringTables: {dict.Count}/{stFiles.Count}");
}

// 2) Localization (en) locres
{
    var locFiles = provider.Files.Keys.Where(p => p.StartsWith("SparkingZERO/Content/Localization/", StringComparison.OrdinalIgnoreCase) && p.Contains("/en/") && p.EndsWith(".locres")).ToList();
    var locOut = new Dictionary<string, object?>();
    foreach (var path in locFiles)
    {
        try
        {
            var data = provider.SaveAsset(path);
            var locres = new FTextLocalizationResource(new FByteArchive(path, data));
            locOut[path] = locres;
        }
        catch (Exception e) { failures.Add($"{path}: {e.Message}"); }
    }
    File.WriteAllText(Path.Combine(OutDir, "locres_en.json"), JsonConvert.SerializeObject(locOut, settings));
    Console.WriteLine($"Locres(en): {locOut.Count}/{locFiles.Count}");
}

// 3) Master data
foreach (var f in simpleFolders) ExportMerged(f);
foreach (var f in groupedFolders) ExportGrouped(f);

File.WriteAllLines(Path.Combine(OutDir, "export_failures.txt"), failures);
Console.WriteLine($"DONE. Failures: {failures.Count}");
