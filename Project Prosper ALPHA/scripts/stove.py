if 'smeltRecipes' not in globals():
    smeltRecipes=[recipe for recipe in recipeObjs if recipe.type=='smelting0']
    #print(smeltRecipes)
def smelt():
    global smeltDone,smelting
    realTime.sleep(5)
    print('done')
    smeltDone=True
    smelting=False
smeltInv=cOb.obData['Inventory']
if smeltInv[1]['Item']==26:
    enemyObjs[1].spawn()
    smeltInv[1]['Amount']-=1
    if smeltInv[1]['Amount']<=0:
        smeltInv[1]['Item']=None
smelting=False
smeltOpen=True

addStack(34,smeltInv[0]['Item'],smeltInv[0]['Amount'])
addStack(35,smeltInv[1]['Item'],smeltInv[1]['Amount'])
addStack(36,smeltInv[2]['Item'],smeltInv[2]['Amount'])



smeltDict=PyEngine.load(PurePath('data','smeltDebug.json'))
smeltList=smeltDict['Positions']
smelt0=pygame.image.load(PurePath('objects','stove','smeltScreen','smelt0.png'))
smelt1=pygame.image.load(PurePath('objects','stove','smeltScreen','smelt1.png'))
smelt2=pygame.image.load(PurePath('objects','stove','smeltScreen','smelt2.png'))
smelt3=pygame.image.load(PurePath('objects','stove','smeltScreen','smelt3.png'))
smelt4=pygame.image.load(PurePath('objects','stove','smeltScreen','smelt4.png'))
smelt5=pygame.image.load(PurePath('objects','stove','smeltScreen','smelt5.png'))
currentSmelt=smelt5
smeltStuff=[lambda:screen.blit(invOverlay,(0,0)),lambda:screen.blit(invOverlay2,(0,32)),lambda:screen.blit(smeltOverlay,(343,51)),lambda:screen.blit(currentSmelt,(0,0)),lambda:blitItems()]