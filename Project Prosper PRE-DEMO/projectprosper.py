import pygame,PyEngine,random,time
#screen=pygame.display.set_mode((512,512))
screen=pygame.display.set_mode((512,512))
pygame.display.set_caption('Project Prosper','idk')

#level0=pygame.image.load('levelPlan.png')
#level1=pygame.image.load('levelPlan.png')
pygame.init()
font=pygame.font.Font('Coure.fon',15)
fastStart=False
newGameStart=False
gameStarting=False
seed=None
done=False
ver=PyEngine.TextBox('Project Prosper PRE-DEMO BUILD',0,487,25,200,'coure.fon',15,False,False,'white','black','white',3,(5,5))
def newGameToggle():
    global newGameStart
    newGameStart=True
def newGame(): 
    print('new game started') 
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit()
        
        screen.fill('black')
        PyEngine.showAll(screen)
        PyEngine.listenAll(screen)
        pygame.display.update()
def options():
    print('No options yet')
def setDistribution(value):
    global distribution
    distribution=value
def startGame():
    global gameStarting,seed,start
    gameStarting=True
    if seedText!='':
        seed=int(seedText)
    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
    screen.fill('black')
    screen.blit(font.render('Generating World...',True,'white'),(200,220))
    pygame.display.update()
    start=time.time()
if not fastStart:
    tips=PyEngine.load('data\\tips.json')
    tip=random.choice(tips)
    tipLines=PyEngine.autoWrap('Tip: '+tip,480,font,'white')
    mainMenuImg=pygame.image.load('misc\\mainMenu.png')
    projectImg=pygame.image.load('misc\\project.png')
    prosperImg=pygame.image.load('misc\\prosper.png')
    mainMenuOverlay=pygame.image.load('misc\\mainMenuOverlay.png')
    tipOverlay=pygame.image.load('misc\\tipOverlay.png')
    tipOverlay.set_alpha(150)
    mainMenuOverlay.set_alpha(150)
    newGameButt=PyEngine.GameButton(200,325,newGameToggle,'default',True,True,'default',64,'misc\\button.png',120,40,None,'misc\\buttonAlt.png')
    optionsButt=PyEngine.GameButton(200,380,options,'default',True,True,'default',64,'misc\\button.png',120,40,None,'misc\\buttonAlt.png')
    exitButt=PyEngine.GameButton(200,435,exit,'default',True,True,'default',64,'misc\\button.png',120,40,None,'misc\\buttonAlt.png')
    seedEntry=PyEngine.GameButton(200,60,pygame.key.start_text_input,'default',True,False,'ibeam',64,'misc\\button.png',120,40,None,None)
    equalButt=PyEngine.GameButton(60,150,lambda:setDistribution('equal'),'default',True,False,'default',64,'misc\\button.png',120,40,None,'misc\\buttonAlt.png')
    oceansButt=PyEngine.GameButton(200,150,lambda:setDistribution('oceans'),'default',True,False,'default',64,'misc\\button.png',120,40,None,'misc\\buttonAlt.png')
    balancedButt=PyEngine.GameButton(340,150,lambda:setDistribution('balanced'),'default',True,False,'default',64,'misc\\button.png',120,40,None,'misc\\buttonAlt.png')
    createWorldButt=PyEngine.GameButton(200,315,startGame,'default',True,False,'default',64,'misc\\button.png',120,40,None,'misc\\buttonAlt.png')
    line=[] 
    seedText=''
    distribution='balanced'
    while not gameStarting:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit()
            if newGameStart and event.type==pygame.TEXTINPUT:
                if event.dict.get('text') in ['0','1','2','3','4','5','6','7','8','9']:
                    line.append(event.dict.get('text'))
                    seedText=''.join(line)
            if newGameStart and event.type==pygame.KEYDOWN:
                keys=pygame.key.get_pressed()
                if keys[pygame.K_BACKSPACE] and len(line)>0:
                    line.pop(-1)
                    seedText=''.join(line)
        screen.blit(mainMenuImg,(0,0))
        screen.blit(mainMenuOverlay,(46,10))
        if not newGameStart:
            screen.blit(projectImg,(60,20))
            screen.blit(prosperImg,(60,150))
        else:
            PyEngine.enableAll()
            exitButt.disable()
            optionsButt.disable()
            newGameButt.disable()
        PyEngine.showAll(screen)
        PyEngine.listenAll(screen)
        if not newGameStart:
            screen.blit(font.render('New Game',True,'white'),(230,335))
            screen.blit(font.render('Options',True,'white'),(230,390))
            screen.blit(font.render('Exit',True,'white'),(245,445))
        elif not gameStarting and newGameStart: 
            screen.blit(font.render('New World',True,'black','white'),(225,20))
            screen.blit(font.render('Seed',True,'white'),(245,40))
            screen.blit(font.render(seedText,True,'white'),(215,72))
            screen.blit(font.render(f'Distribution: {distribution}',True,'white'),(180,120))
            screen.blit(font.render(f'Equal',True,'white'),(100,162))
            screen.blit(font.render(f'Oceans',True,'white'),(235,162))
            screen.blit(font.render(f'Balanced',True,'white'),(365,162))
            #Equal Description
            equalText=PyEngine.autoWrap('Equal: All biomes have an equal chance of generating',120,font,'white')
            for i in range(len(equalText)):
                screen.blit(equalText[i],(55,200+i*20))
            oceanText=PyEngine.autoWrap('Oceans: oceans are more likely to appear',120,font,'white')
            for i in range(len(oceanText)):
                screen.blit(oceanText[i],(195,200+i*20))
            balText=PyEngine.autoWrap('Balanced: Biomes balanced for a more balanced playthrough (Recommended)',150,font,'white')
            for i in range(len(balText)):
                screen.blit(balText[i],(335,200+i*20))    
            screen.blit(font.render('Create World',True,'white'),(210,325))
            screen.blit(tipOverlay,(5,360))
            for i in range(len(tipLines)):
                screen.blit(tipLines[i],(10,370+20*i))
        ver.render(screen)
        pygame.display.update()
#print(pygame.font.get_fonts())
grass=pygame.image.load('biomes\\grass.png')
ocean=pygame.image.load('biomes\\ocean.png')
desert=pygame.image.load('biomes\\desert.png')
forest=pygame.image.load('biomes\\forest.png')

slash0=pygame.image.load('Slash\\slash0.png')
slash1=pygame.image.load('Slash\\slash1.png')
slash2=pygame.image.load('Slash\\slash2.png')
slash3=pygame.image.load('Slash\\slash3.png')
slash4=pygame.image.load('Slash\\slash4.png')
slash5=pygame.image.load('Slash\\slash5.png')
slash6=pygame.image.load('Slash\\slash6.png')
slash7=pygame.image.load('Slash\\slash7.png')

slashL0=pygame.image.load('SlashLeft\\slash0.png')
slashL1=pygame.image.load('SlashLeft\\slash1.png')
slashL2=pygame.image.load('SlashLeft\\slash2.png')
slashL3=pygame.image.load('SlashLeft\\slash3.png')
slashL4=pygame.image.load('SlashLeft\\slash4.png')
slashL5=pygame.image.load('SlashLeft\\slash5.png')
slashL6=pygame.image.load('SlashLeft\\slash6.png')
slashL7=pygame.image.load('SlashLeft\\slash7.png')

tree0=pygame.image.load('objects\\tree\\tree\\tree0.png')
tree1=pygame.image.load('objects\\tree\\tree\\tree1.png')
tree2=pygame.image.load('objects\\tree\\tree\\tree2.png')
tree3=pygame.image.load('objects\\tree\\tree\\tree3.png')
tree4=pygame.image.load('objects\\tree\\tree\\tree4.png')

stone0=pygame.image.load('objects\\stone\\stone\\stone0.png')
stone1=pygame.image.load('objects\\stone\\stone\\stone1.png')
stone2=pygame.image.load('objects\\stone\\stone\\stone2.png')
stone3=pygame.image.load('objects\\stone\\stone\\stone3.png')
stone4=pygame.image.load('objects\\stone\\stone\\stone4.png')

bush0=pygame.image.load('objects\\bush\\bush\\bush0.png')
bush1=pygame.image.load('objects\\bush\\bush\\bush1.png')
bush2=pygame.image.load('objects\\bush\\bush\\bush2.png')
bush3=pygame.image.load('objects\\bush\\bush\\bush3.png')
bush4=pygame.image.load('objects\\bush\\bush\\bush4.png')


invOverlay=pygame.image.load('objects\\invOverlay.png')
invOverlay2=pygame.image.load('objects\\invOverlay2.png')
invOverlay3=pygame.image.load('objects\\craftOverlay.png')
hbOverlay=pygame.image.load('objects\\hotBarOverlay.png')
invScreen=pygame.image.load('objects\\invScreen3.png')
hotBar=pygame.image.load('objects\\hotBar.png')
hotBarSelector=pygame.image.load('objects\\hotBarSelector.png')

invOverlay.set_alpha(150)
invOverlay2.set_alpha(200)
invOverlay3.set_alpha(200)
hbOverlay.set_alpha(200)

test=pygame.image.load('objects\\test.png')
hbvis=pygame.image.load('misc\\hitboxVis.png')
hbvisBig=pygame.image.load('misc\\hitboxVisBig.png')
hbvisNone=pygame.image.load('misc\\hitboxVisNone.png')
hbvisBigNone=pygame.image.load('misc\\hitboxVisNoneBig.png')
hbvisBigBlock=pygame.image.load('misc\\hitboxVisBigBlock.png')

slash=[slash0,slash1,slash2,slash3,slash4,slash5,slash6,slash7]
slashL=[slashL0,slashL1,slashL2,slashL3,slashL4,slashL5,slashL6,slashL7]
tree=[tree0,tree1,tree2,tree3,tree4]
stone=[stone0,stone1,stone2,stone3,stone4]
bush=[bush0,bush1,bush2,bush3,bush4]

woodSprite=pygame.image.load('items\\wood.png')
obstacle=pygame.image.load('objects\\tree\\tree.png')
stoneBig=pygame.image.load('objects\\stone\\stone.png')
bushBig=pygame.image.load('objects\\bush\\bush.png')
cactus=pygame.image.load('objects\\cactus.png')
woodWall=pygame.image.load('objects\\woodWall.png')

placedObjects={'tree':obstacle,'cactus':cactus,'woodWall':woodWall,'stone':stoneBig,'bush':bushBig}

placedItemMap={'woodWall':2}

placeItemMapRev={placedItemMap[i]:i for i in placedItemMap}

selectorPos=1
debugInv=False
quickGen=True
snapToMouse=False
valid=False
invFull=False
tileRects=[]
craftRects=[]
tiles=[]
obRects=[]
droppedItems=[]
itemObjs=[]
blockObjs=[]
recipeObjs=[]
mapMode=False
frame=0
fframe=0
invOpen=False
holdingItem=False
#key: white=naturally generated,black=none,blue=block
drawHitboxes=False
ii=0
playerImg=pygame.image.load('biomes\\bigPlayer.png')
pygame.display.set_icon(pygame.image.load('misc\\icon.png'))
#enemies=[]
recipes=PyEngine.load('data\\recipes.json')
items=PyEngine.load('data\\items.json')
blocks=PyEngine.load('data\\blocks.json')
#0-17 Normal slots, 18-23 hotbar slots, 24+ crafting slots
inventory=[{'Slot':0,'Item':None,'Amount':0},{'Slot':1,'Item':None,'Amount':0},{'Slot':2,'Item':None,'Amount':0},{'Slot':3,'Item':None,'Amount':0},{'Slot':4,'Item':None,'Amount':0},{'Slot':5,'Item':None,'Amount':0},{'Slot':6,'Item':None,'Amount':0},{'Slot':7,'Item':None,'Amount':0},{'Slot':8,'Item':None,'Amount':0},{'Slot':9,'Item':None,'Amount':0},{'Slot':10,'Item':None,'Amount':0},{'Slot':11,'Item':None,'Amount':0},{'Slot':12,'Item':None,'Amount':0},{'Slot':13,'Item':None,'Amount':0},{'Slot':14,'Item':None,'Amount':0},{'Slot':15,'Item':None,'Amount':0},{'Slot':16,'Item':None,'Amount':0},{'Slot':17,'Item':None,'Amount':0},{'Slot':18,'Item':None,'Amount':0},{'Slot':19,'Item':None,'Amount':0},{'Slot':20,'Item':None,'Amount':0},{'Slot':21,'Item':None,'Amount':0},{'Slot':22,'Item':None,'Amount':0},{'Slot':23,'Item':None,'Amount':0},{'Slot':24,'Item':None,'Amount':0},{'Slot':25,'Item':None,'Amount':0},{'Slot':26,'Item':None,'Amount':0},{'Slot':27,'Item':None,'Amount':0},{'Slot':28,'Item':None,'Amount':0},{'Slot':29,'Item':None,'Amount':0},{'Slot':30,'Item':None,'Amount':0},{'Slot':31,'Item':None,'Amount':0},{'Slot':32,'Item':None,'Amount':0},{'Slot':33,'Item':None,'Amount':0}]
def customRound(x,base):
    return base * round(x/base)
clock=pygame.time.Clock()
class Player:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.currentBiome='unknown'
        self.playerRect=pygame.rect.Rect(self.x,self.y,32,32)
    def listenInputs(self):
            keys=pygame.key.get_pressed()
            blockMovement=False
            if keys[pygame.K_d]:
                futureRect=self.playerRect.copy()
                futureRect.move_ip(4,0)
                for obstacle in obstacles:
                    if obstacle.colisRect.colliderect(futureRect):
                        if obstacle.type=='woodWall':
                            #print(obstacle.colisRect.top,obstacle.colisRect.left)
                            #print(futureRect.top,futureRect.left)
                            blockMovement=True
                            break
                if not blockMovement:
                    self.x+=2
                        
                screen.blit(playerImg,(self.x,self.y))
            if keys[pygame.K_a]:
                blockMovement=False
                futureRect=self.playerRect.copy()
                futureRect.move_ip(-4,0)
                for obstacle in obstacles:
                    if obstacle.colisRect.colliderect(futureRect):
                        if obstacle.type=='woodWall':
                            #print(obstacle.colisRect.top,obstacle.colisRect.left)
                            #print(futureRect.top,futureRect.left)
                            blockMovement=True
                            break
                else:
                    blockMovement=False
                if not blockMovement:
                    self.x-=2
                screen.blit(playerImg,(self.x,self.y))
            screen.blit(playerImg,(self.x,self.y))
            if keys[pygame.K_w]:
                blockMovement=False
                futureRect=self.playerRect.copy()
                futureRect.move_ip(0,-4)
                for obstacle in obstacles:
                    if obstacle.colisRect.colliderect(futureRect):
                        if obstacle.type=='woodWall':
                            #print(obstacle.colisRect.top,obstacle.colisRect.left)
                            #print(futureRect.top,futureRect.left)
                            blockMovement=True
                            break
                if not blockMovement:
                    self.y-=2
                screen.blit(playerImg,(self.x,self.y))
            if keys[pygame.K_s]:
                blockMovement=False
                futureRect=self.playerRect.copy()
                futureRect.move_ip(0,4)
                for obstacle in obstacles:
                    if obstacle.colisRect.colliderect(futureRect):
                        if obstacle.type=='woodWall':
                            #print(obstacle.colisRect.top,obstacle.colisRect.left)
                            #print(futureRect.top,futureRect.left)
                            blockMovement=True
                            break
                if not blockMovement:
                    self.y+=2
                screen.blit(playerImg,(self.x,self.y))
            self.playerRect=pygame.rect.Rect(self.x,self.y,32,32)
    def getBiome(self):
        for tile in tiles:
            if tile.checkCollisions():
                self.id=tile.id
                print(player.id)
    
    pygame.display.update()
def generate():
    global screen,seed,distribution,start
    levelMap=[]
    if fastStart:
        distribution='balanced'
        start=time.time()
    if not quickGen:
        seed=input('Seed:')
    if seed is None or seed=='':
        seed=random.choice(range(10**18,10**18*10))
        random.seed(seed)
    else:
        if seed=='survival island' or seed==123:
            levelMap=['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o',
                      'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 
                      'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 
                      'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 
                      'o', 'o', 'o', 'o', 'o', 'o', 'o', 'd', 'd', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 
                      'o', 'o', 'o', 'o', 'o', 'o', 'd', 'g', 'g', 'd', 'o', 'o', 'o', 'o', 'o', 'o', 
                      'o', 'o', 'o', 'o', 'o', 'd', 'g', 'g', 'g', 'g', 'd', 'o', 'o', 'o', 'o', 'o', 
                      'o', 'o', 'o', 'o', 'd', 'g', 'g', 'g', 'g', 'g', 'g', 'd', 'o', 'o', 'o', 'o', 
                      'o', 'o', 'o', 'd', 'g', 'g', 'g', 'f', 'f', 'g', 'g', 'g', 'd', 'o', 'o', 'o', 
                      'o', 'o', 'o', 'o', 'd', 'g', 'g', 'g', 'g', 'g', 'g', 'd', 'o', 'o', 'o', 'o', 
                      'o', 'o', 'o', 'o', 'o', 'd', 'g', 'g', 'g', 'g', 'd', 'o', 'o', 'o', 'o', 'o', 
                      'o', 'o', 'o', 'o', 'o', 'o', 'd', 'g', 'g', 'd', 'o', 'o', 'o', 'o', 'o', 'o', 
                      'o', 'o', 'o', 'o', 'o', 'o', 'o', 'd', 'd', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 
                      'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 
                      'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 
                      'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o']
        if seed=='test' or seed=='69':
            levelMap=['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o',
                      'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 
                      'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 
                      'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 
                      'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 
                      'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 
                      'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 
                      'o', 'o', 'o', 'o', 'o', 'f', 'f', 'g', 'g', 'd', 'd', 'o', 'o', 'o', 'o', 'o', 
                      'o', 'o', 'o', 'o', 'o', 'f', 'f', 'g', 'g', 'd', 'd', 'o', 'o', 'o', 'o', 'o', 
                      'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 
                      'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 
                      'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 
                      'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 
                      'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 
                      'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 
                      'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o']
        random.seed(seed)
    print(f'Seed: {seed}')
    possibilites=[]
    choice='o'
    x=0
    y=0
    if not levelMap:
        for i in range(256):
            if distribution=='equal' and mapMode:
                possibilites=['o','f','g','d']
                possibilites.append(choice)
                possibilites.append(choice)
                choice=random.choice(possibilites)
                tiles.append(Tile(x*32,y*32,choice,i))
                levelMap.append(choice)
            elif distribution=='oceans'and mapMode:
                possibilites=['o','o','o','o','f','g','d']
                possibilites.append(choice)
                possibilites.append(choice)
                choice=random.choice(possibilites)
                tiles.append(Tile(x*32,y*32,choice,i))
                levelMap.append(choice)
            elif distribution=='balanced' and mapMode:
                possibilites=['o','o','f','f','g','g','g','d']
                possibilites.append(choice)
                possibilites.append(choice)
                choice=random.choice(possibilites)
                tiles.append(Tile(x*32,y*32,choice,i))
                levelMap.append(choice)
            elif distribution=='equal' and not mapMode:
                possibilites=['o','f','g','d']
                possibilites.append(choice)
                possibilites.append(choice)
                choice=random.choice(possibilites)
                tiles.append(Tile(x*512,y*512,choice,i))
                levelMap.append(choice)
            elif distribution=='oceans'and not mapMode:
                possibilites=['o','o','o','f','g','d']
                possibilites.append(choice)
                possibilites.append(choice)
                choice=random.choice(possibilites)
                tiles.append(Tile(x*512,y*512,choice,i))
                levelMap.append(choice)
            elif distribution=='balanced' and not mapMode:
                possibilites=['o','o','o','f','f','g','g','g','d']
                possibilites.append(choice)
                possibilites.append(choice)
                choice=random.choice(possibilites)
                tiles.append(Tile(x*512,y*512,choice,i))
                levelMap.append(choice)
            if x==15:
                y+=1
                x=0
                if y==16:
                    break 
                continue 
            x+=1      
        random.seed()
        print(time.time()-start)
        return levelMap
    else:
        i=0
        for biome in levelMap:
            tiles.append(Tile(x*512,y*512,biome,i))
            i+=1
            if x==15:
                y+=1
                x=0
                if y==16:
                    return levelMap 
                continue 
            x+=1 
def blitBiome():
    for tile in tiles:
        if tile.id==player.id:
            tile.loadTile()
class Item:
    def __init__(self,itemId:int):
        self.itemId=itemId
        self.data=items[self.itemId]
        self.name=self.data['Name']
        self.maxStackSize=self.data['MaxStackSize']
        self.spriteLocation=self.data['Sprite']
        self.sprite=pygame.image.load('items\\'+self.spriteLocation)
        self.type=self.data['Type']
    def pickUp(self):
        global invFull
        inventory.reverse()
        for item in inventory[10:]:
            if item['Slot']>24:
                invFull=True
                break
            if item['Item']==self.itemId and item['Amount']<self.maxStackSize:
                item['Amount']+=1
                #print(item)
                
                break
            elif item['Item']is None:
                item['Item']=self.itemId
                item['Amount']+=1
                break
        inventory.reverse()
for item in items:
    itemObjs.append(Item(item['Id']))
class Recipe:
    def __init__(self,recipeId):
        self.recipeId=recipeId
        self.data=recipes[self.recipeId]
        self.name=self.data['Name']
        self.recipe=self.data['Recipe']
        self.output=self.data['Output']
        self.shapeless=self.data['Shapeless']
        self.count=self.data['Count']
        self.items=[]
        self.craftItems=[]
    def checkRecipe(self,craftingInv:list):
        self.items.clear()
        self.craftItems.clear()
        if not self.shapeless:
            if craftingInv==self.recipe:
                return True
            return False
        elif self.shapeless:
            for item in self.recipe:
                if item is not None:
                    self.items.append(item)
            for item in craftingInv:
                if item is not None:
                    self.craftItems.append(item)
            self.items.sort()
            self.craftItems.sort()
            if self.items==self.craftItems:
                return True
            return False
for recipe in recipes:
    recipeObjs.append(Recipe(recipe['Id']))
class Obstacle:
    def __init__(self,type,rect,id,dropsItem) -> None:
        self.type=type
        self.id=id
        if self.type=='tree':
            if rect.left>=20:
                self.colisRect=pygame.rect.Rect(rect.left+20,rect.top,rect.width,rect.height)
            else:
                self.colisRect=pygame.rect.Rect(0,rect.top,rect.width,rect.height)
            self.rect=rect
        else:
            self.rect=rect
            self.colisRect=rect
        self.dropsItem=dropsItem
    def checkCollisionDamage(self,rect,animation,doAnimation,getLocation,destorySelf):
        if self.colisRect.colliderect(rect):
            
                #PyEngine.animation(tree,8,5,screen,self.rect.left,self.rect.top)
            if destorySelf:
                for tile in tiles:
                    if tile.id==player.id:
                        #print(self.id)
                        tile.obstacles.pop(self.id)
                        tile.obstacles.insert(self.id,Obstacle('none',self.colisRect,self.id,None))  
            if doAnimation:      
                for i in range(len(animation)):
                    screen.fill('white')
                    for tile in tiles:
                        if tile.id==player.id:
                            tile.loadTile()
                    screen.blit(animation[i],self.rect)
                    screen.blit(playerImg,(player.x,player.y))
                    currentItem=inventory[selectorPos+17]
                    screen.blit(hbOverlay,(0,0))
                    for item in inventory[18:24]:
                        if item['Item'] is not None:
                            screen.blit(getItem(item['Item']).sprite,hbList[item['Slot']-18])
                            if item['Amount']>1:
                                screen.blit(font.render(str(item['Amount']),True,'white'),(hbList[item['Slot']-18][0]-2,hbList[item['Slot']-18][1]+26))
                        screen.blit(hotBar,(0,0))
                        screen.blit(hotBarSelector,(hbList[selectorPos-1][0]-1,hbList[selectorPos-1][1]-1))
                    for item in droppedItems:
                        if item != True and item !=False:
                            if item['Type'] is not None:
                                screen.blit(getItem(item['Type']).sprite,(item['Position'].left+32,item['Position'].top+32))
                    ver.render(screen)
                    pygame.display.update()
                    clock.tick(8)
            if getLocation:
                #print(self.dropsItem)
                return {'Type':self.dropsItem,'Position':self.rect}
            return True,self.type
        return False
    def interact(self):
        for block in blockObjs:
            if block.name==self.type:
                if block.script is not None:
                    exec(block.script)
class Tile:
    def __init__(self,x,y,biome,id):
        self.x=x
        self.y=y
        self.biome=biome
        self.obRects=[]
        #Append new tiles with the cave biome and bind them to the entrances
        if self.biome=='g':
            self.color=pygame.image.load('biomes\\grass.png')
        elif self.biome=='f':
            self.color=pygame.image.load('biomes\\forest.png')
        elif self.biome=='d':
            self.color=pygame.image.load('biomes\\desert.png')
        elif self.biome=='o':
            self.color=pygame.image.load('biomes\\ocean.png')   
        self.id=id
        if mapMode:
            self.tileRect=pygame.Rect(self.x,self.y,32,32)
        if not mapMode:
            self.tileRect=pygame.Rect(self.x,self.y,512,512)
        tileRects.append(self.tileRect)
        self.obstacles=[]
        self.createObstacles()
    def checkCollisions(self):
        #print(tileRects)
        #print(self.playerRect.collidelist(tileRects))
        if player.playerRect.colliderect(self.tileRect):
            player.currentBiome=self.biome
            #screen.blit(self.color,(self.x,self.y),)
            #print(f'Current Biome: {player.currentBiome}')
            #print(f'id: {self.id}')
            print('god help me')
            return True
            
        else:
            return False
    def createObstacles(self):
        global seed
        self.obstacles=[]
        if self.biome=='g':
            x=0
            y=0
            
            
            for i in range(256):
                type=random.choice(['none','none','none','tree','stone','none','none','bush','none','none'])
                if type=='tree':
                    dropsItem=1
                elif type=='stone':
                    dropsItem=3
                elif type=='bush':
                    dropsItem=5
                else:
                    dropsItem=0
                if type=='tree':
                    self.obstacles.append(Obstacle(type,pygame.rect.Rect((x*64-20,y*64),(64,64)),i,dropsItem))
                else:
                    self.obstacles.append(Obstacle(type,pygame.rect.Rect((x*64,y*64),(64,64)),i,dropsItem))
                if x==15:
                    y+=1
                    x=0
                    if y==32:
                        break
                    continue 
                x+=1 
        elif self.biome=='f':
            x=0
            y=0
            
            
            for i in range(256):
                type=random.choice(['none','tree','bush'])
                if type=='tree':
                    dropsItem=1
                elif type=='stone':
                    dropsItem=3
                elif type=='bush':
                    dropsItem=5
                else:
                    dropsItem=0
                if type=='tree':
                    self.obstacles.append(Obstacle(type,pygame.rect.Rect((x*64-20,y*64),(64,64)),i,dropsItem))
                else:
                    self.obstacles.append(Obstacle(type,pygame.rect.Rect((x*64,y*64),(64,64)),i,dropsItem))
                if x==15:
                    y+=1
                    x=0
                    if y==32:
                        break
                    continue 
                x+=1 
        elif self.biome=='o':
            x=0
            y=0
            
            
            for i in range(256):
                type=random.choice(['none'])
                if type=='tree':
                    dropsItem=1
                elif type=='stone':
                    dropsItem=3
                else:
                    dropsItem=0
                self.obstacles.append(Obstacle(type,pygame.rect.Rect((x*64,y*64),(64,64)),i,dropsItem))
                if x==15:
                    y+=1
                    x=0
                    if y==32:
                        break
                    continue 
                x+=1 
        elif self.biome=='d':
            x=0
            y=0
            
            
            for i in range(256):
                type=random.choice(['none','none','cactus'])
                if type=='tree':
                    dropsItem=1
                elif type=='stone':
                    dropsItem=3
                else:
                    dropsItem=0
                self.obstacles.append(Obstacle(type,pygame.rect.Rect((x*64,y*64),(64,64)),i,dropsItem))
                if x==15:
                    y+=1
                    x=0
                    if y==32:
                        break
                    continue 
                x+=1 
        #print(len(self.obstacles))
    def loadTile(self):
        global obRects
        screen.blit(self.color,(0,0))
        for obstaclee in self.obstacles:
            if obstaclee.type != 'none':
                screen.blit(placedObjects[obstaclee.type],obstaclee.rect)
            #if obstaclee.type=='tree':
            #    screen.blit(obstacle,obstaclee.rect)
            #elif obstaclee.type=='cactus':
            #    screen.blit(cactus,obstaclee.rect)       
    def getObstacles(self):
        return self.obstacles
class Block(Obstacle):
    def __init__(self,id):
        self.id=id
        self.data=blocks[self.id]
        self.name=self.data['Name']
        self.sprite=pygame.image.load(self.data['Sprite'])
        self.parentItem=getItem(self.data['ParentId'])
        if self.data['Script'] is not None:
            self.script=compile(open(self.data['Script']+'.py').read(),self.data['Script']+'.py','exec')
        else:
            self.script=None
    #def addToObstacles(self,obstacles:list,index):
    #    obstacles.insert(index,self.name)

def getBlock(id:int)-> Block:
    return blockObjs[id]              
def getItem(id:int)-> Item:
    return itemObjs[id]
for block in blocks:
    blockObjs.append(Block(block['Id']))
def loadLevel(level):
    x=0
    y=0
    screen.fill('white')
    for i in level:
        if i=='g':
            screen.blit(grass,(x*32,y*32))
        if i=='o':
            screen.blit(ocean,(x*32,y*32))
        if i=='d':
            screen.blit(desert,(x*32,y*32))
        if i=='f':
            screen.blit(forest,(x*32,y*32))    
        if x==15:
            y+=1
            x=0
            if y==16:
                break 
            continue
        x+=1
level=generate()
player=Player(256,256)
player.id=128
tBox=PyEngine.TextBox('Unknown',0,0,32,64,'Coure.fon',25,False,False,'black','grey','black',3,(5,10))
while True:
    for tile in tiles:
        if tile.id==player.id:
            currentTile=tile
            obstacles=tile.obstacles
    #What was this even
    #if mapMode:
    #    for i in tiles:
    #        if i.checkCollisions():
    #            if not mapMode:
    #                i.loadTile()
    #            break
    if player.y>512-32:
        player.y=0
        player.id+=16
        droppedItems.clear()
        print(player.id)
    elif player.y<0:
        player.y=512-32
        player.id-=16
        droppedItems.clear()
        print(player.id)
    elif player.x>512-32:
        player.x=0
        player.id+=1
        droppedItems.clear()
        print(player.id)
    elif player.x<0:
        player.x=512-32
        player.id-=1
        droppedItems.clear()
        print(player.id)
    if mapMode:
        loadLevel(level)
    else:
        blitBiome()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
        if event.type==pygame.KEYDOWN:
            keys=pygame.key.get_pressed()
            if keys[pygame.K_F5] and mapMode:
                level=generate()
            elif keys[pygame.K_F5] and not mapMode:
                for tile in tiles:
                    if tile.id==player.id:
                        tile.createObstacles()
            if keys[pygame.K_F4]:
                if not drawHitboxes:
                    drawHitboxes=True
                elif drawHitboxes:
                    drawHitboxes=False
            if keys[pygame.K_e]:
                if not invOpen:
                    invOpen=True
                elif invOpen:
                    invOpen=False
        currentItem=inventory[selectorPos+17]
        if event.type==pygame.MOUSEBUTTONDOWN and not invOpen:
            currentItem=inventory[selectorPos+17]
            mouseRect=pygame.Rect((pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1]),(8,8))
            if currentItem['Item'] is not None and event.dict['button']==1:
                if getItem(currentItem['Item']).type=='Block':
                    #print('ur mom')
                    for block in blockObjs:
                        if block.parentItem==getItem(currentItem['Item']):
                            currentBlock=block
                            for i in range(len(obstacles)):
                                obData=obstacles[i].checkCollisionDamage(mouseRect,None,False,False,False)
                                #print(obData)
                                if obData!=False:
                                    if obData[0]:
                                        #print('ur dad')
                                        oldob=obstacles.pop(i)
                                        obstacles.insert(i,Obstacle(currentBlock.name,oldob.rect,oldob.id,2))
                                        currentItem['Amount']-=1
                                        if currentItem['Amount']==0:
                                            currentItem['Item']=None
                                        break
            if event.dict['button']==3:
                for obstacle in obstacles:
                    obData=obstacle.checkCollisionDamage(mouseRect,None,False,False,False)
                    if obData!=False:
                        if obData[0]:
                            obstacle.interact()                   
            if pygame.mouse.get_pos().__getitem__(0)>player.x and event.dict['button']==1 and currentItem['Item']==8: 
                for frame in range(len(slash)):
                    screen.fill('white')
                    blitBiome()
                    screen.blit(slash[frame],(player.x+20,player.y))
                    screen.blit(playerImg,(player.x,player.y))
                    currentItem=inventory[selectorPos+17]
                    screen.blit(hbOverlay,(0,0))
                    for item in inventory[18:24]:
                        if item['Item'] is not None:
                            screen.blit(getItem(item['Item']).sprite,hbList[item['Slot']-18])
                        screen.blit(hotBar,(0,0))
                        screen.blit(hotBarSelector,(hbList[selectorPos-1][0]-1,hbList[selectorPos-1][1]-1))
                        for item in droppedItems:
                            if item != True and item !=False:
                                if item['Type'] is not None:
                                    screen.blit(getItem(item['Type']).sprite,(item['Position'].left+32,item['Position'].top+32))
                    ver.render(screen)
                    pygame.display.update()
                    clock.tick(16)
                slashRect=pygame.rect.Rect(player.x+20,player.y,32,32)
                for ob in obstacles:
                    if ob.type=='tree':
                        droppedItems.append(ob.checkCollisionDamage(slashRect,tree,True,True,True))
                        droppedItems.append(droppedItems[-1])
                    if ob.type=='stone':
                        droppedItems.append(ob.checkCollisionDamage(slashRect,stone,True,True,True)) 
                        droppedItems.append(droppedItems[-1])
                    if ob.type=='bush':
                        droppedItems.append(ob.checkCollisionDamage(slashRect,bush,True,True,True))
                        droppedItems.append(droppedItems[-1])
            elif event.dict['button']==1 and currentItem['Item']==None: 
                        for ob in obstacles:
                            if ob.type=='tree':
                                droppedItems.append(ob.checkCollisionDamage(mouseRect,tree,True,True,True))
                            if ob.type=='stone':
                                droppedItems.append(ob.checkCollisionDamage(mouseRect,stone,True,True,True)) 
                            if ob.type=='bush':
                                droppedItems.append(ob.checkCollisionDamage(mouseRect,bush,True,True,True))   
            elif pygame.mouse.get_pos().__getitem__(0)<=player.x and event.dict['button']==1 and currentItem['Item']==8:
                for frame in range(len(slashL)):
                    screen.fill('white')
                    blitBiome()
                    screen.blit(slashL[frame],(player.x-23,player.y))
                    screen.blit(playerImg,(player.x,player.y))
                    currentItem=inventory[selectorPos+17]
                    screen.blit(hbOverlay,(0,0))
                    for item in inventory[18:24]:
                        if item['Item'] is not None:
                            screen.blit(getItem(item['Item']).sprite,hbList[item['Slot']-18])
                        screen.blit(hotBar,(0,0))
                        screen.blit(hotBarSelector,(hbList[selectorPos-1][0]-1,hbList[selectorPos-1][1]-1))
                        for item in droppedItems:
                            if item != True and item !=False:
                                if item['Type'] is not None:
                                    screen.blit(getItem(item['Type']).sprite,(item['Position'].left+32,item['Position'].top+32))
                    ver.render(screen)
                    pygame.display.update()
                    clock.tick(16)
                slashRect=pygame.rect.Rect(player.x-23,player.y,32,32)
                for ob in obstacles:
                    if ob.type=='tree':
                        droppedItems.append(ob.checkCollisionDamage(slashRect,tree,True,True,True)) 
                        droppedItems.append(droppedItems[-1])
                    if ob.type=='stone':
                        droppedItems.append(ob.checkCollisionDamage(slashRect,stone,True,True,True))
                        droppedItems.append(droppedItems[-1])
                    if ob.type=='bush':
                        droppedItems.append(ob.checkCollisionDamage(slashRect,bush,True,True,True))
                        droppedItems.append(droppedItems[-1])
            elif  event.dict['button']==4:
                if selectorPos>1:
                    selectorPos-=1
                else:
                    selectorPos=6
            elif event.dict['button']==5:
                if selectorPos<6:
                    selectorPos+=1
                else:
                    selectorPos=1
        elif event.type==pygame.MOUSEBUTTONDOWN and invOpen:
            slotHover=pygame.Rect(pygame.mouse.get_pos(),(16,16)).collidelist(invRects)
            #1 = LMB
            #2 = MMB
            #3 = RMB
            if event.dict['button']==1:
                #If output clicked
                if slotHover==33 and inventory[slotHover]['Item']is not None and not holdingItem and valid:
                    for nothing in inventory[24:33]:
                        if nothing['Item']is not None:
                            nothing['Amount']-=1
                            if nothing['Amount']==0:
                                nothing['Item']=None
                    holdingItem=True
                    heldItem=getItem(inventory[slotHover]['Item'])
                    heldItemAmount=inventory[slotHover]['Amount']
                    inventory[slotHover]['Item']=None
                    inventory[slotHover]['Amount']=0
                elif slotHover==33 and holdingItem:
                    pass
                #If slot with a item clicked empty handed
                elif slotHover>-1 and inventory[slotHover]['Item']is not None and not holdingItem:
                    holdingItem=True
                    heldItem=getItem(inventory[slotHover]['Item'])
                    heldItemAmount=inventory[slotHover]['Amount']
                    inventory[slotHover]['Item']=None
                    inventory[slotHover]['Amount']=0
                #Add item count if possible
                elif slotHover>-1 and inventory[slotHover]['Item']==heldItem.itemId and holdingItem and inventory[slotHover]['Amount']+heldItemAmount<=heldItem.maxStackSize:
                    holdingItem=False
                    inventory[slotHover]['Amount']+=heldItemAmount
                #Switch held item
                elif slotHover>-1 and inventory[slotHover]['Item']!=heldItem.itemId and inventory[slotHover]['Item']is not None and holdingItem:
                    #holdingItem=False
                    tempItem=heldItem
                    tempItemAmount=heldItemAmount
                    heldItem=getItem(inventory[slotHover]['Item'])
                    heldItemAmount=inventory[slotHover]['Amount']
                    inventory[slotHover]['Item']=tempItem.itemId
                    inventory[slotHover]['Amount']=tempItemAmount
                    #Drop item if click outside inventory area
                #Place item in empty slot
                elif slotHover>-1 and inventory[slotHover]['Item']is None and holdingItem and inventory[slotHover]['Amount']<=heldItem.maxStackSize:
                    holdingItem=False
                    inventory[slotHover]['Item']=heldItem.itemId
                    inventory[slotHover]['Amount']=heldItemAmount
            if event.dict['button']==3:
                if slotHover>-1 and inventory[slotHover]['Item']is not None and not holdingItem:
                    holdingItem=True
                    heldItem=getItem(inventory[slotHover]['Item'])
                    heldItemAmount=1
                    inventory[slotHover]['Amount']-=1
                    if inventory[slotHover]['Amount']<=0:
                        inventory[slotHover]['Item']=None
                elif slotHover>-1 and inventory[slotHover]['Item']==heldItem.itemId and holdingItem and inventory[slotHover]['Amount']+heldItemAmount<=heldItem.maxStackSize:
                    holdingItem=False
                    inventory[slotHover]['Amount']+=heldItemAmount
                elif slotHover>-1 and inventory[slotHover]['Item']is None and holdingItem and inventory[slotHover]['Amount']<=heldItem.maxStackSize:
                    heldItemAmount-=1
                    if heldItemAmount==0:
                        holdingItem=False
                    inventory[slotHover]['Item']=heldItem.itemId
                    inventory[slotHover]['Amount']+=1
    mouseRect=pygame.Rect((pygame.mouse.get_pos()[0]-16,pygame.mouse.get_pos()[1]-16),(8,8))
    if currentItem['Item'] is not None:
        if getItem(currentItem['Item']).type=='Block':
            for block in blockObjs:
                if block.parentItem==getItem(currentItem['Item']):
                    currentBlock=block
                    for i in range(len(obstacles)):
                        if obstacles[i].checkCollisionDamage(mouseRect,None,False,False,False):
                            hover=currentBlock.sprite.copy()
                            hover.set_alpha(130)
                            screen.blit(hover,(customRound(mouseRect.left,64),customRound(mouseRect.top,64)))
                            break            
    invDict=PyEngine.load('data\\InvDebug.json')
    invList=invDict['positions']
    craftDict=PyEngine.load('data\\craftDebug.json')
    craftList=craftDict['positions']
    hbDict=PyEngine.load('data\\hotBarDebug.json')
    hbList=hbDict['positons']
    invRects=[]
    for slot in invList:
        invRects.append(pygame.Rect(slot,(32,32)))
    for slot in craftList:
        invRects.append(pygame.Rect(slot,(32,32)))
    invPositions=[]
    player.listenInputs()
    while None in droppedItems:
        droppedItems.remove(None)
    for item in droppedItems:
        if item != True and item !=False:
            if item['Type'] is not None:
                screen.blit(getItem(item['Type']).sprite,(item['Position'].left+32,item['Position'].top+32))
                if player.playerRect.colliderect(item['Position']) and not invFull:
                    droppedItems.remove(item)
                    getItem(item['Type']).pickUp()
    if invOpen:
        screen.blit(invOverlay,(0,0))
        screen.blit(invOverlay2,(0,32))
        screen.blit(invOverlay3,(300,32))
        screen.blit(invScreen,(0,0))
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        if debugInv:
            xx=8
            yy=48
            for i in range(18):
                invPositions.append((xx,yy))
                xx+=44
                if ii>4:
                    yy+=52
                    xx=8
                    ii=0
                    continue
                ii+=1
            invDict.update(positions=invPositions)
            print(invDict)
            PyEngine.save('InvDebug.json',invDict)
        else:
            for item in inventory:
                if item['Item'] is not None:
                    screen.blit(getItem(item['Item']).sprite,invList[item['Slot']])
                    if item['Amount']>1:
                        screen.blit(font.render(str(item['Amount']),True,'white'),(invList[item['Slot']][0]-4,invList[item['Slot']][1]+24))
                    elif item['Amount']<=0:
                        item['Item']=None
            craftingGrid=[]
            for something in inventory[24:33]:
                craftingGrid.append(something['Item'])
            for recipe in recipeObjs:
                valid=recipe.checkRecipe(craftingGrid)
                if valid:
                    inventory[33]['Item']=recipe.output
                    inventory[33]['Amount']=recipe.count
                    break
                else:
                    inventory[33]['Item']=None
                    inventory[33]['Amount']=0
            if holdingItem:
                screen.blit(heldItem.sprite,pygame.mouse.get_pos())
                if holdingItem and heldItemAmount>1:
                    screen.blit(font.render(str(heldItemAmount),True,'white'),(pygame.mouse.get_pos()[0]-4,pygame.mouse.get_pos()[1]+24))
            slotHover=pygame.Rect(pygame.mouse.get_pos(),(16,16)).collidelist(invRects)
            if slotHover>-1 and inventory[slotHover]['Item']is not None and not holdingItem:
                tBox.update(getItem(inventory[slotHover]['Item']).name)
                tBox.snapToMouse(512)
                tBox.render(screen,True)
    else:
        #Hot bar
        currentItem=inventory[selectorPos+17]
        screen.blit(hbOverlay,(0,0))
        for item in inventory[18:24]:
            if item['Item'] is not None:
                screen.blit(getItem(item['Item']).sprite,hbList[item['Slot']-18])
                if item['Amount']>1:
                    screen.blit(font.render(str(item['Amount']),True,'white'),(hbList[item['Slot']-18][0]-2,hbList[item['Slot']-18][1]+26))
        screen.blit(hotBar,(0,0))
        screen.blit(hotBarSelector,(hbList[selectorPos-1][0]-1,hbList[selectorPos-1][1]-1))
        if currentItem['Item'] is not None:
            itemText=PyEngine.TextBox(getItem(currentItem['Item']).name,5,60,25,50,'Coure.fon',25,False,False,'black',None,None,0,(0,0))
            itemText.render(screen)
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        else:
            pygame.mouse.set_cursor(pygame.cursors.Cursor((8,8),pygame.image.load('misc\\hand.png')))
        if drawHitboxes:
            screen.blit(hbvis,player.playerRect)
            for obstacle in obstacles:
                try:
                    if obstacle.type=='none':
                        screen.blit(hbvisBigNone,obstacle.colisRect)
                    elif obstacle.type=='tree'or obstacle.type=='stone'or obstacle.type=='bush' or obstacle.type=='cactus':
                        screen.blit(hbvisBig,obstacle.colisRect)
                    else:
                        screen.blit(hbvisBigBlock,obstacle.colisRect)
                except:
                    pass
    ver.render(screen,True)
    pygame.display.update()
    clock.tick(60)