#print('l')
currentTool.durability-=1
currentTool.reloadSprite()
if currentTool.durability==0:
    removeStack(currentIndex)