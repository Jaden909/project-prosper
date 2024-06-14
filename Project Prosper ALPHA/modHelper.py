'''Helper functions for mods to add things to the game'''
from pathlib import PurePath
import json
exec(compile(open(PurePath('core','Item.py')).read(),'Item.py','exec'),globals())
exec(compile(open(PurePath('core','Tool.py')).read(),'Tool.py','exec'),globals())

def registerItems(itemPath):
    '''Register a list of items to the game. Returns a list of the Ids the items were assigned'''
    itemIds={'relative':[],'actual':[]}
    items=json.load(open(PurePath('mods',itemPath)))
    for item in items:
        if item['Type']=='Tool':
            itemIds['relative'].append(items.index(item))
            itemIds['actual'].append(len(itemObjs))
            tool=Tool(items.index(item),itemPath)
            tool.itemId=len(itemObjs)
            itemObjs.append(tool)    
        else:
            
            itemIds['relative'].append((items.index(item)))
            itemIds['actual'].append(len(itemObjs))
            itemm=Item(items.index(item),itemPath)
            itemm.itemId=len(itemObjs)
            if 'Object failed to load' in itemm.name:
                itemm.name=f'Object failed to load ({itemm.itemId})'
            itemObjs.append(itemm)
    return itemIds