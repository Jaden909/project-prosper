# Project Prosper
A survival game about rapidly advancing technology



# Modding Documentation
### Note: Modding is not yet officially supported, this is being written now so it is ready for when it IS supported.

## Setting up a Mod (not fully working yet)
1. Create a folder with the name of your mod
   
2. Create a new .py file in the new folder (you can also name this after your mod but it doesn't matter)
   
3. Copy this line of code into the python file: 
   ```python
   exec(compile(open('modHelper.py').read(),'modHelper.py','exec'),globals())
   ```
   This will intialize the modHelper script in a way that will allow it to access the game's variables directly
   
4. You should now be able to use modHelper's functions (though your IDE won't know and say the functions are undefined)
   
5. If you have items that you want added to game, use this line of code:
   ```python
   registerItems(json.load(open('moditems.json')),'moditems.json')
   ```
   replace 'moditems.json' with the path to the json file containing your items' data (relative to the Project Prosper ALPHA folder)
   
6. You have now added your own items to the game! `registerItems()` returns both the id of the items relative to the mod and the actual id that was assigned when it was added to the game. You can use these in your mod logic.  

  
#### Classes that are/will be moddable:
## `Item`
###### Values:
`Name`: Name that is displayed in game (required)

`Id`: id of the item, automatically generated when using the `itemTool` script (required)

`MaxStackSize`: the maximum amount of items allowed in a stack, can theoretically be any number greater than 0 (required)

`Sprite`: the filename of the items sprite (required)

`Type`: the type of item, automatically determined when using the `itemTool` script (required, can be either 'Item','Block','Tool')

`Tooltip`: the tooltip of the item (optional)

`Tags`: the item's tags (optional, see list of valid tags below)

Valid tags for `Item`:
* `durability`* - How many times the item can be used before breaking
* `harvestLevel`* - Up to what level of obstacle can it break
* `lscript`* - Script to run on left click when holding this item
* `rscript`* - Script to run on right click when holding this item
* `damage`* - Amount of damage done to enemies
* `solidFuel` - Signifies a solid furnace fuel source (value doesn't matter, it just checks for the existence of this tag)
* `burnTime` - How many frames this item will fuel a furnace <br>
\* Item must be a tool
 
Note that the only way of making modded items obtainable currently is adding recipes which make them (which isn't currently supported anyway)

A valid example of a new item would be:
```json
{"Name": "Axe", "Id": 0, "MaxStackSize": 1, "Sprite": "axe.png", "Type": "Item", "Tags": {"durability":50, "harvestLevel":1, "lscript":"l.py", "rscript":"r.py", "damage":10}}
```
