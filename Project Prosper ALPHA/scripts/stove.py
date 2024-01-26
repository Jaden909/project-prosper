if 'smeltRecipes' not in globals():
    smeltRecipes=[recipe for recipe in recipeObjs if recipe.type=='smelting0']
    print(smeltRecipes)
def smelt():
    global smeltDone,smelting
    time.sleep(5)
    print('done')
    smeltDone=True
    smelting=False
smelting=False
smeltOpen=True
smeltDict=PyEngine.load('data\\smeltDebug.json')
smeltList=smeltDict['Positions']
smelt0=pygame.image.load('objects\\stove\\smeltScreen\\smelt0.png')
smelt1=pygame.image.load('objects\\stove\\smeltScreen\\smelt1.png')
smelt2=pygame.image.load('objects\\stove\\smeltScreen\\smelt2.png')
smelt3=pygame.image.load('objects\\stove\\smeltScreen\\smelt3.png')
smelt4=pygame.image.load('objects\\stove\\smeltScreen\\smelt4.png')
smelt5=pygame.image.load('objects\\stove\\smeltScreen\\smelt5.png')
currentSmelt=smelt5
smeltStuff=[lambda:screen.blit(invOverlay,(0,0)),lambda:screen.blit(invOverlay2,(0,32)),lambda:screen.blit(currentSmelt,(0,0)),lambda:blitItems()]