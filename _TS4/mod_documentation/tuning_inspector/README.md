#  Tuning Inspector

Insect the loaded tuning files which are converted to Python objects. Most settings which are in the XML files are readable this way.
The inspector doesn't allow to modify any settings.

## Usage of the Tuning Inspector

'inspect - suntan_BeachTowel' - the mod will figure out that you meant manager 'interaction'.
'inspect INTERACTION suntan_BeachTowel' - to look at the tuning
'inspect INTERACTION suntan_BeachTowel test_globals' - to drill down into the test_globals property.
'inspect INTERACTION suntan_BeachTowel test_globals.LocationTest' - to drill further down into the test_globals and then the LocationTest property.

The output can be overwhelming and digging into properties may not always be possible.
Some fixes and checks for special cases could be added if really needed.


# Addendum

## Game compatibility
This mod has been tested with `The Sims 4`  1.98.158, S4CL 2.7, TS4Lib 0.0.24.
It is expected to be compatible with many upcoming releases of TS4, S4CL and TS4Lib.

## Dependencies
* [S4CL](https://github.com/ColonolNutty/Sims4CommunityLibrary/releases/latest)
* [TS4Lib](https://github.com/Oops19/TS4-Library/releases/latest)

If not installed download and install these mods.

## Installation
* Locate the localized `The Sims 4` folder which contains the `Mods` folder.
* Extract the ZIP file into this `The Sims 4` folder.
* It will create the directories/files `Mods/_o19_/$mod_name.ts4script`, `Mods/_o19_/$mod_name.package`, `mod_data/$mod_name/*` and/or `mod_documentation/$mod_name/*`
* `mod_logs/$mod_name.txt` will be created as soon as data is logged.

### Manual Installation
If you don't want to extract the ZIP file into `The Sims 4` folder you might want to read this. 
* The files in `ZIP-File/mod_data` are usually required and should be extracted to `The Sims 4/mod_data`.
* The files in `ZIP-File/mod_documentation` are for you to read it. They are not needed to use this mod.
* The `Mods/_o19_/*.ts4script` files can be stored in a random folder within `Mods` or directly in `Mods`. I highly recommend to store it in `_o19_` so you know who created it.

## Usage Tracking / Privacy
This mod does not send any data to tracking servers. The code is open source, not obfuscated, and can be reviewed.

Some log entries in the log file ('mod_logs' folder) may contain the local username, especially if files are not found (WARN, ERROR).

## External Links
[Sources](https://github.com/Oops19/)
[Support](https://discord.gg/d8X9aQ3jbm)
[Donations](https://www.patreon.com/o19)

## Copyright and License
* © 2023 [Oops19](https://github.com/Oops19)
* License for '.package' files: [Electronic Arts TOS for UGC](https://tos.ea.com/legalapp/WEBTERMS/US/en/PC/)  
* License for other media unless specified differently: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) unless the Electronic Arts TOS for UGC overrides it.
This allows you to use this mod and re-use the code even if you don't own The Sims 4.
Have fun extending this mod and/or integrating it with your mods.

Oops19 is not endorsed by or affiliated with Electronic Arts or its licensors.
Game content and materials copyright Electronic Arts Inc. and its licensors. 
Trademarks are the property of their respective owners.

### TOS
* Please don't put it behind a paywall.
* Please don't create mods which break with every TS4 update.
* For simple tuning modifications use [Patch-XML](https://github.com/Oops19/TS4-PatchXML) or [LiveXML](https://github.com/Oops19/TS4-LiveXML).
* To check custom tunings use [VanillaLogs](https://github.com/Oops19/TS4-VanillaLogs).
