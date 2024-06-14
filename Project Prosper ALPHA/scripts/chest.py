chestMenu=pygame.image.load(PurePath('Objects','chestScreen.png'))
chestOpen=True
chestInv=cOb.obData['Inventory']
for i in range(15):
    addStack(i+37,chestInv[i]['Item'],chestInv[i]['Amount'])
#Generate loot

chestStuff=[lambda:screen.blit(invOverlay,(0,0)),lambda:screen.blit(invOverlay2,(0,32)),lambda:screen.blit(chestOverlay,(271,43)),lambda:screen.blit(chestMenu,(0,0)),lambda:blitItems()]