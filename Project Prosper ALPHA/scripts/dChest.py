chestMenu=pygame.image.load(PurePath('Objects','chestScreen.png'))
chestOpen=True
chestInv=cOb.obData['Inventory']
if 'gen' not in cOb.obData:
    random.seed(seed)
    for slot in chestInv:
        num=random.choice(range(1,101))
        for item in cOb.obData['LootTable']:
            if num<item['chance']:
                slot['Item']=item['item']
                slot['Amount']=random.choice(item['amount'])
                break
        else:
            slot['Item']=None
            slot['Amount']=0
    cOb.obData['gen']=None
    random.seed()
for i in range(15):
    addStack(i+37,chestInv[i]['Item'],chestInv[i]['Amount'])
#Generate loot

chestStuff=[lambda:screen.blit(invOverlay,(0,0)),lambda:screen.blit(invOverlay2,(0,32)),lambda:screen.blit(chestOverlay,(271,43)),lambda:screen.blit(chestMenu,(0,0)),lambda:blitItems()]