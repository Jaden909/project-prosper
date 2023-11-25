# Project Prosper
A survival game 



# Modding Documentation
### Note: Modding is not yet officially supported, this is being written now so it is ready for when it IS supported.
#### Classes that are/will be moddable:
#### `Item`
###### Values:
`Name`: Name that is displayed in game (required)

`Id`: id of the item, automatically generated when using the `itemTool` script (required)

`MaxStackSize`: the maximum amount of items allowed in a stack, can theoretically be any number greater than 0 (required)

`Sprite`: the filename of the items sprite (required)

`Type`: the type of item, automatically determined when using the `itemTool` script (required, can be either 'Item','Block','Tool')

Note that it is not yet possible to add methods of obtaining these items

A valid example of a new item would be:
```json
{"Name": "Axe", "Id": 0, "MaxStackSize": 1, "Sprite": "axe.png", "Type": "Item"}
```
