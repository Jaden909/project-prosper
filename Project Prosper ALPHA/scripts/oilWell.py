oilUi=pygame.image.load(PurePath('misc','ui','oilWellUi.png'))
oilOverlay=pygame.image.load(PurePath('misc','ui','oilOverlay.png'))
oilOverlay.set_alpha(200)
oilInv=cOb.obData['Inventory']



if 'oilRun' not in globals():
    oilRun=0
else:
    oilRun+=1
def drill():
    global oilInv
    while True:
        realTime.sleep(5)
        if oilInv[0]['Item'] is None:
            oilInv[0]['Item']=43
            oilInv[0]['Amount']=1
            #addStack(52,43,1)
        elif oilInv[0]['Amount']<getItem(43).maxStackSize and oilInv[0]['Item']==43:
            oilInv[0]['Amount']+=1
            
    #print('done')


try:
    inventory[52]
except IndexError:
    inventory.append({'Slot':52,'Item':None,'Amount':0})
if oilInv[0]['Item']==43:
    addStack(52,oilInv[0]['Item'],oilInv[0]['Amount'])
def oilInvLoop():
    global oilInv
    screen.blit(invOverlay,(0,0))
    screen.blit(invOverlay2,(0,32))
    screen.blit(oilOverlay,(0,0))
    screen.blit(oilUi,(0,0))
    slots=list(range(24))
    slots.extend([52])
    getSlot(slots)
    removeStack(52)
    addStack(52,oilInv[0]['Item'],oilInv[0]['Amount'])
    blitItems()
    oilInv=syncInvs(oilInv,(52,53))
    cOb.obData['Inventory']=oilInv 
def oilWellLoop(event):
    if event.type==pygame.MOUSEBUTTONDOWN:
            print('bruh')
            slots=list(range(24))
            slots.append(52)
            removeStack(52)
            invLoop(slots) 
def close():
    global oilInv
    print(oilInv)
    oilInv=syncInvs(oilInv,(52,53))
    print(oilInv)
    cOb.obData['Inventory']=oilInv
    try:
        removeStack(52)
    except:
        pass
    uiQueue.clear()
    eventQueue.clear()
    closeQueue.clear()
if 'Thread' not in cOb.obData:
        cOb.obData['Thread']=threading.Thread(target=drill)
        cOb.obData['Thread'].start()

#else:
#    print(cOb.obData['Thread'])            

uiQueue.append(oilInvLoop)
eventQueue.append(oilWellLoop)

closeQueue.append(close)
#scriptQueue.append(drill)