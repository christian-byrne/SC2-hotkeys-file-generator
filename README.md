# SC2 Auto HK Setup


###### Table of Contents

- [Reasons to Use](#reasons-to-use)
- [Usage](#usage)
- [Credits & How this was Made](#credits--how-this-was-made)
  - [Hotkey File Template](#hotkey-file-template)
  - [Clean Data](#clean-data)
  - [Save as json File](#save-as-json-file)
  - [Classifying Hotkey Assignments by Race](#classifying-hotkey-assignments-by-race)
  - [Code Script](#code-script)
  - [Other Features that can Be Easily Implemented](#other-features-that-can-be-easily-implemented)
- [To Do](#to-do)


*Automates the process of generating SC2 hotkey files which adhere to some sort of universal logic.* 


Currently only works by supporting a grid defined by user. In other words, there is a 4x5 grid when you select a unit/building and look at the abilities/options in the bottom right of the UI -- the user can assign a hotkey for each position in that grid so that it's consistent across all units/buildings. Other types of logic can easily be implemented, however -- but probably doesn't require code in those cases.

**Note**: Issues or desired features => create a post. I only tested this on my own system because I didn't want to download SC2 on my other computers, so apologies for possible bugs. Hopefully you can stil figure out how the script generally works by reading this page -- and then use the info and the files in the repo to solve your problems. Many possible uses for the script could be replaced by some smart search/replace logic or Regex, especially if you look at the json file as a reference first. GLHF.


## Reasons to Use

<details>
    <summary>Click to Expand</summary>

- Allows you to add two-key hotkeys for all actions, which is not possible in the options screen of SC2 (may have changed since I wrote this.)
  - For example, add hotkey `Ctrl+D` to make a drone -- not possible usually but this script allows it
- Create hotkeys that correspond to universal grid-based logic
  - This is the most common suggestion/tip I found when researching guides and forum posts about using the best hotkey setup.
- Saves time
  - Since this mass changes all hotkeys, it saves you from the tedious process of individually changing each hotkey
  - You may then be more willing to experiment with different setups knowing that it won't be tedious creating new profiles
- Automatically creates a hotkey file that you can drag and drop to your `C:\Users\User\Documents\Starcraft II\User\Hotkeys` Folder
  - The profile will then be uploaded to the cloud and be accessible on any computer
  - Doesn't force you to rewrite any existing hotkey setups

</details>

## Usage

1. Create a folder somewhere
1. Open a terminal/cmd 
1. Copy the file path of the folder you created (`Ctrl+L` then `Ctrl+C` in Windows File Explorer, for example) 
1. type `cd file_path` in the terminal, replace `file_path` with the path you just copied. You may need to enclose the file path in quotes if it has spaces
1. Get this repository's clone address (the green drop down at the top of the page that says `code`)
1. Type `git clone URL` in terminal, replacing `URL` with the URL you copied from previous step
1. Enter `cd sc2-hotkeys` in terminal
1. Download python3 if you do not have it
1. In terminal, type:

```bash
# Unix/MacOS
python3 grid.py

# Windows
py grid.py
```

10. Follow instructions that appear in the terminal
11. The output file will be in the same folder you are in (`sc2-hotkeys` folder). There are two example files there already (`zerg-control-grid.SC2Hotkeys` and `zerg-shift-grid.SC2Hotkeys`)
12. Drag and drop the output file (its extension should be `.SC2Hotkeys`) to your SC2 Hotkeys folder ([See: Where is sc2 hotkey folder on my computer?](https://liquipedia.net/starcraft2/Hotkeys#:~:text=Hotkeys%20are%20stored%20in%20the,your%20Windows%20My%20Documents%20folder.)). If you've never made any custom hotkeys, you may need to create a new hotkey profile in the SC2 game and make a single change, and the folder will be generated. 
13. Restart/start the game. In SC2 game, go to `Menu` -> `Options` -> `Hotkeys` -> `Select Profile`
14. click `ignore` if prompted about hotkey conflicts.
14. Select the newly created profile and click `Accept`

***Note*** - You may also want to look at the hotkey files already in your hotkey folder and then copy paste some of the options at the top of the file into the newly created file (things like custom control groups and camera control which this script does not generate hotkeys for).

## Credits & How this was Made


##### Hotkey File Template

Found [BurnySc2's repo](https://github.com/BurnySc2/SC2Hotkeys) which contained custom hotkey files for all races using a grid layout. 

Lists the identifiers for all the hotkeys and has them assigned to a value correspdonding to the `/qwer/asdf/zxcv/` grid


##### Clean Data

Used vim to convert all the hotkey values in those files to standard array syntax. 

> (`Shift+]` to select paragraphs in block visual mode --> paste a `"`at start of every line. Then do a search replace on newline characters `\r` with `",\r` to add comma and end quote). Probably a faster way. Might also be faster to just use an line-tools helper website like [this](http://www.unit-conversion.info/texttools/add-prefix-into-line/#data) to add custom prefix/suffix to every line.

##### Save as `json` File

Save the formatted data to a [json file](./raw-grid-assignments.json) for efficiency. Import python `json` module and add function to read in data.

##### Classifying Hotkey Assignments by Race

Data is organized alphabetically. So I need a key that maps races to their units and buildings in order to categorize the raw data from the json file. 

Searched "SC2 Zerg Units" to find a wiki site that listed units/buildings with minimal markup and preferably not in an HTML table. Found a relatively unformatted list in the third result at [strategywiki.org](https://strategywiki.org/wiki/StarCraft_II:_Wings_of_Liberty/Zerg_buildings) for each race's buildings and units.

Copy and pasted the data into [text files for each race.](./units-building)

Added function to read, parse and organize the data into python structures. The data was numbered so just had to create copies of each line and filter out any character that wasn't alpha.

##### Code Script

Get preferences from user at stdin. 

Get all hotkeys for the user's race. Map them to their position in the grid to the grid provided by the user of the default grid (wherein `q/w/e/r` is the first row).

Then re-map hotkeys with user's defined grid. 

Add feature to prefix each hotkey with a second key (e.g., `Ctrl`, `Shift`) -- this is my original reason for writing this script. 

Write the new hotkey assignments to the Blizzard hotkey file filetype. Filename (provided by user) will be the `Hotkey Profile` in Sc2 Menus (automatically uploaded to cloud and accessible on any computer IIRC).

##### Other Features that can Be Easily Implemented

The groundwork is there to add other features for automating the process of creating custom hotkeys that adhere to some rule system like the grid. 

## To Do

- Other layout systems
- Auto move file to correct folder
- Test on other system