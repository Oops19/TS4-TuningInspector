# Tuning Inspector

This mod allows to inspect the loaded tuning files which are converted to Python objects. Most settings which are in the XML files are readable this way.
The inspector doesn't allow to modify any settings.

## Audience
* Mod authors who create and/or patch tuning files can use this mod to verify the modification.
* Mod aod authors who shamelessly copy EA code to modify one line and then paste it in a tuning are also welcome to use this mod. But please don't do this, it is not nice to break the game of other players with every TS4 update. Use Patch-XML and create mods which don't break the game.

This mod is not intended to be installed and used by people who want to play The Sims 4. It doesn't modify the game play at all. It offers read-only access to loaded tuning objects.

## Usage of the Tuning Inspector

If you plan to modify location tests for the beach towel it's easy to edit the XML and edit some elements.
Anyhow, it might be hard to test whether the changes do actually work and have been properly imported.

Here are some commands to look into the tuning object which is used in-game:
'inspect - suntan_BeachTowel' - the mod will figure out that you meant manager 'interaction'.
'inspect INTERACTION suntan_BeachTowel' - to look at the tuning. You will notice that there are 'test_globals'.
'inspect INTERACTION suntan_BeachTowel test_globals' - to drill down into the test_globals property. You will notice that 'LocationTest' is one of the possible tests.
'inspect INTERACTION suntan_BeachTowel test_globals.LocationTest' - to drill further down into the test_globals and then into the LocationTest property.

The output can be overwhelming and digging into XML properties is not always be possible. Some tests are converted to test objects in TS4 and can not be found in the tuning.
With PatchXML one can patch these tests during load-time. With Live-XML patching such tests is very tricky. 

With this public release both TS4Lib and this mod will no longer be bundled with Live-XML or Patch-XML.

### Examples
#### Faster Gardening - Tutorial for a Live XML mod


## Compatibility

This mod is incompatible with the [inspector](https://modthesims.info/showthread.php?t=575118) tool by [scumbumbo](https://modthesims.info/m/7401825) as the same 'inspect' cheat command is used.

I made it incompatible on purpose as the original inspector is a script to edit, reload, edit, reload to inspect the tuning. I did this many times while it wasn't too much fun.

This inspector accepts the classes/tuples/... to look into directly as a parameter which avoids endless script editing and reloading.



# Addendum

## Game compatibility
This mod has been tested with `The Sims 4` 1.118.257, S4CL 3.15, TS4Lib 0.3.42.
It is expected to be compatible with many upcoming releases of TS4, S4CL and TS4Lib.

## Dependencies
Download the ZIP file, not the sources.
* [This Mod](../../releases/latest)
* [TS4-Library](https://github.com/Oops19/TS4-Library/releases/latest)
* [S4CL](https://github.com/ColonolNutty/Sims4CommunityLibrary/releases/latest)
* [The Sims 4](https://www.ea.com/games/the-sims/the-sims-4)

If not installed download and install TS4 and these mods.
All are available for free.

## Removal of the mod
The mod installation with unzip writes to a few directories.
To remove this mod and all related files locate the files and folders and remove them:
* `The Sims 4/Mods/_o19_/$mod_name.*`
* `The Sims 4/mod_data/_o19_/$mod_name/`
* `The Sims 4/mod_documentation/_o19_/$mod_name/`
* `The Sims 4/mod_sources/_o19_/$mod_name/`

To remove all of my mods locate these folders and remove them:
* `The Sims 4/Mods/_o19_/`
* `The Sims 4/mod_data/_o19_/`
* `The Sims 4/mod_documentation/_o19_/`
* `The Sims 4/mod_sources/_o19_/`
 
## Installation
* Locate the localized `The Sims 4` folder which contains the `Mods` folder.
* Extract the ZIP file into this `The Sims 4` folder.
* It will create the directories/files `Mods/_o19_/$mod_name.ts4script`, `Mods/_o19_/$mod_name.package`, `mod_data/$mod_name/*` and/or `mod_documentation/$mod_name/*` and/or `mod_sources/$mod_name/*`
* CAS and build-buy UGC without scripts will create `Mods/o19/$mod_name.package`.
* `mod_logs/$mod_name.txt` will be created as soon as data is logged.
* `mod_documentation/$mod_name/` and/or `mod_sources/$mod_name/` are not required and can be deleted.

### Manual Installation
If you don't want to extract the ZIP file into `The Sims 4` folder you might want to read this.
You can extract the ZIP file to a temporary directory and copy the folders manually.
* The files in `ZIP-File/mod_data` are usually required and should be extracted to `The Sims 4/mod_data`.
* The files in `ZIP-File/mod_documentation` are for you to read it. They are not needed to use this mod.
* The files in `ZIP-File/mod_sources` are not needed to use this mod.
* The `Mods/_o19_/*.ts4script` files can be stored in a random folder within `Mods` or directly in `Mods`. I highly recommend to store it in `_o19_` so you know who created it.

## Troubleshooting
When installed properly this is not necessary at all.
For manual installations check these things and make sure each question can be answered with 'yes'.
* Does 'The Sims 4' (localized to Die Sims 4, Les Sims 4, Los Sims 4, The Sims 4, ...) exist?
  * Does `The Sims 4` contain the folder `Mods`?
    * Does `Mods` contain the folder `_o19_`? 
      * Does `_19_` contain `ts4lib.ts4script` and `ts4lib.package` files?
      * Does `_19_` contain `{mod_name}.ts4script` and/or `{mod_name}.package` files?
  * Does `The Sims 4` contain the folder `mod_data`?
    * Does `mod_data` contain the folder `{mod_name}`?
      * Does `{mod_name}` contain files or folders?
  * Does `The Sims 4` contain the `mod_logs` ?
    * Does `mod_logs` contain the file `Sims4CommunityLib_*_Messages.txt`?
    * Does `mod_logs` contain the file `TS4-Library_*_Messages.txt`?
      * Is this the most recent version or can it be updated?
    * Does `mod_logs` contain the file `{mod_name}_*_Messages.txt`?
      * Is this the most recent version or can it be updated?
  * Doesn't `The Sims 4` contain the file(s) `last_exception.txt`  and/or `last_exception*.txt` ?
* Share the `The Sims 4/mod_logs/Sims4CommunityLib_*_Messages.txt` and `The Sims 4/mod_logs/{mod_name}_*_Messages.txt`  file.

## Usage Tracking / Privacy
This mod does not send any data to tracking servers. The code is open source, not obfuscated, and can be reviewed.

Some log entries in the log file ('mod_logs' folder) may contain the local username, especially if files are not found (WARN, ERROR).

## External Links
[Sources](https://github.com/Oops19/)
[Support](https://discord.gg/d8X9aQ3jbm)
[Donations](https://www.patreon.com/o19)

## Copyright and License
* © 2020-2025 [Oops19](https://github.com/Oops19)
* License for '.package' files: [Electronic Arts TOS for UGC](https://tos.ea.com/legalapp/WEBTERMS/US/en/PC/)  
* License for other media unless specified differently: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) unless the Electronic Arts TOS for UGC overrides it.
This allows you to use this mod and re-use the code even if you don't own The Sims 4.
Have fun extending this mod and/or integrating it with your mods.

Oops19 / o19 is not endorsed by or affiliated with Electronic Arts or its licensors.
Game content and materials copyright Electronic Arts Inc. and its licensors. 
Trademarks are the property of their respective owners.

### TOS
* Please don't put it behind a paywall.
* Please don't create mods which break with every TS4 update.
* For simple tuning modifications use [Patch-XML](https://github.com/Oops19/TS4-PatchXML) 
* or [LiveXML](https://github.com/Oops19/TS4-LiveXML).
* To check the XML structure of custom tunings use [VanillaLogs](https://github.com/Oops19/TS4-VanillaLogs).
