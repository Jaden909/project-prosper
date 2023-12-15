import pygame,PyEngine,random,time,ctypes,os,sys,threading
ctypes.windll.shcore.SetProcessDpiAwareness(0)
pygame.init()
#screen=pygame.display.set_mode((512,512))
screen=pygame.display.set_mode((512,512))
pygame.display.set_caption('Project Prosper','idk')
horn0=pygame.mixer.Sound('sfx\\horn0.wav')
horn1=pygame.mixer.Sound('sfx\\horn1.wav')
horn2=pygame.mixer.Sound('sfx\\horn2.wav')
horn3=pygame.mixer.Sound('sfx\\horn3.wav')
horns=[horn0,horn1,horn2,horn3]


#Seasonal Events
currentTime=time.localtime()
eventActive=False
#xmas=False
print(currentTime[1],currentTime[2])
if currentTime[1]==12 and currentTime[2]==1:
    eventItems=[14]
    eventActive=True
elif currentTime[1]==12 and currentTime[2] in range(15,25):
    xmas=True
    eventActive=True
    eventItems=[17]
def emuSeason(items):
    global eventActive,eventItems
    eventActive=True
    eventItems=items
    
#Use to emulate seasonal events
#emuSeason([17])
smeltDone=False  
cOb=None
fueled=False
font=pygame.font.Font('Coure.fon',15)
fastStart=False
newGameStart=False
gameStarting=False
seed=None
currentRecipe=None
done=False
inStruct=False
tilesLoaded=0
smeltOpen=False
obCache={}
fuel=0
maxFuel=0
ver=PyEngine.TextBox('Project Prosper ALPHA BUILD',0,487,25,200,'coure.fon',15,False,False,'white','black','white',3,(5,5))
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
    global gameStarting,seed,start,newGameToggle,newGame,options,setDistribution,mainMenuImg,mainMenuOverlay,newGameButt,optionsButt,exitButt,seedEntry,equalButt,oceansButt,balancedButt,createWorldButt
    gameStarting=True
    if seedText!='':
        seed=int(seedText)
    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
    del newGameToggle,newGame,options,setDistribution,mainMenuImg,mainMenuOverlay,newGameButt,optionsButt,exitButt,seedEntry,equalButt,oceansButt,balancedButt,createWorldButt
    screen.fill('black')
    screen.blit(font.render('Generating World...',True,'white'),(200,220))
    pygame.display.update()
    start=time.time()
if not fastStart:
    if not xmas:
        mainMenuImg=pygame.image.load('misc\\mainMenu.png')
        projectImg=pygame.image.load('misc\\project.png')
    else:
        mainMenuImg=pygame.image.load('misc\\mainMenuXmas.png')
        projectImg=pygame.image.load('misc\\projectXmas.png')
    prosperImg=pygame.image.load('misc\\prosper.png')
    mainMenuOverlay=pygame.image.load('misc\\mainMenuOverlay.png')
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
            #screen.blit(tipOverlay,(5,360))
            
        ver.render(screen)
        pygame.display.update()
#print(pygame.font.get_fonts())
grass=pygame.image.load('biomes\\grass.png').convert()
ocean=pygame.image.load('biomes\\ocean.png').convert()
desert=pygame.image.load('biomes\\desert.png').convert()
forest=pygame.image.load('biomes\\forest.png').convert()

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


#cactus=pygame.image.load('objects\\cactus.png')
woodWall=pygame.image.load('objects\\woodWall.png')
caveWall=pygame.image.load(random.choice(['objects\\caveWall.png','objects\\caveWall2.png','objects\\caveWall3.png']))
cave=pygame.image.load('objects\\mine.png')
none64=pygame.image.load('misc\\none64.png')

#placedObjects={'tree':obstacle,'woodWall':woodWall,'stone':stoneBig,'bush':bushBig,'caveWall':caveWall,'mine':cave,'escape':none64}

#placedItemMap={'woodWall':2}

#placeItemMapRev={placedItemMap[i]:i for i in placedItemMap}

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
obstacleData=PyEngine.load('data\\obstacles.json')
#0-17 Normal slots, 18-23 hotbar slots, 24+ crafting slots
inventory=[{'Slot':0,'Item':12,'Amount':1},{'Slot':1,'Item':None,'Amount':0},{'Slot':2,'Item':None,'Amount':0},{'Slot':3,'Item':None,'Amount':0},{'Slot':4,'Item':None,'Amount':0},{'Slot':5,'Item':None,'Amount':0},{'Slot':6,'Item':None,'Amount':0},{'Slot':7,'Item':None,'Amount':0},{'Slot':8,'Item':None,'Amount':0},{'Slot':9,'Item':None,'Amount':0},{'Slot':10,'Item':None,'Amount':0},{'Slot':11,'Item':None,'Amount':0},{'Slot':12,'Item':None,'Amount':0},{'Slot':13,'Item':None,'Amount':0},{'Slot':14,'Item':None,'Amount':0},{'Slot':15,'Item':None,'Amount':0},{'Slot':16,'Item':None,'Amount':0},{'Slot':17,'Item':None,'Amount':0},{'Slot':18,'Item':None,'Amount':0},{'Slot':19,'Item':None,'Amount':0},{'Slot':20,'Item':None,'Amount':0},{'Slot':21,'Item':None,'Amount':0},{'Slot':22,'Item':None,'Amount':0},{'Slot':23,'Item':None,'Amount':0},{'Slot':24,'Item':None,'Amount':0},{'Slot':25,'Item':None,'Amount':0},{'Slot':26,'Item':None,'Amount':0},{'Slot':27,'Item':None,'Amount':0},{'Slot':28,'Item':None,'Amount':0},{'Slot':29,'Item':None,'Amount':0},{'Slot':30,'Item':None,'Amount':0},{'Slot':31,'Item':None,'Amount':0},{'Slot':32,'Item':None,'Amount':0},{'Slot':33,'Item':None,'Amount':0}]
def customRound(x,base):
    return base * round(x/base)
clock=pygame.time.Clock()


def generate():
    global screen,seed,distribution,start,structures
    tips=PyEngine.load('data\\tips.json')
    tip=random.choice(tips)
    tipLines=PyEngine.autoWrap('Tip: '+tip,480,font,'white')
    tipOverlay=pygame.image.load('misc\\tipOverlay.png')
    tipOverlay.set_alpha(150)
    print('Starting World Gen...')
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
    structures=[]
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
                #print(f'Tile {i} Created')
                if choice=='g':
                    choice2=random.choice(['cave'])
                    structures.append(Structure(choice2,i,3,[2,3,4,5,18,19,20,21,34,35,36,37]))
                else:
                    structures.append(Structure('none',i))
                levelMap.append(choice)
            elif distribution=='oceans'and not mapMode:
                possibilites=['o','o','o','f','g','d']
                possibilites.append(choice)
                possibilites.append(choice)
                choice=random.choice(possibilites)
                tiles.append(Tile(x*512,y*512,choice,i))
                #print(f'Tile {i} Created')
                if choice=='g':
                    choice2=random.choice(['cave'])
                    structures.append(Structure(choice2,i,3,[2,3,4,5,18,19,20,21,34,35,36,37]))
                else:
                    structures.append(Structure('none',i))
                levelMap.append(choice)
            elif distribution=='balanced' and not mapMode:
                possibilites=['o','o','o','f','f','g','g','g','d']
                possibilites.append(choice)
                possibilites.append(choice)
                choice=random.choice(possibilites)
                tiles.append(Tile(x*512,y*512,choice,i))
                #print(f'Tile {i} Created')
                if choice=='g':
                    choice2=random.choice(['cave'])
                    structures.append(Structure(choice2,i,3,[2,3,4,5,18,19,20,21,34,35,36,37]))
                else:
                    structures.append(Structure('none',i))
                levelMap.append(choice)
            if x==15:
                y+=1
                x=0
                if y==16:
                    break 
                continue 
            x+=1
            pygame.event.get()
            screen.fill('black')
            progressBar=pygame.surface.Surface((round(tilesLoaded*225/255),32))
            progressBar.fill('green')
            screen.blit(progressBar,(150,400))
            screen.blit(font.render('Generating World...',True,'white'),(200,220))
            screen.blit(font.render(f'Loaded Tile {tilesLoaded} out of 255',True,'white'),(150,450))
            
            for i in range(len(tipLines)):
                screen.blit(tipLines[i],(25,25+i*25))

            pygame.display.update() 
        for tile in tiles:
            print(sys.getsizeof(tile.obstacles))     
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
    print(sys.getsizeof(tiles[3].obstacles[0].sprite)) 

exec(compile(open('core\\Player.py').read(),'core\\Player.py','exec'),globals())
exec(compile(open('core\\Item.py').read(),'core\\Item.py','exec'),globals())
for item in items:
    itemObjs.append(Item(item['Id']))
exec(compile(open('core\\Recipe.py').read(),'core\\Recipe.py','exec'),globals())
for recipe in recipes:
    recipeObjs.append(Recipe(recipe['Id']))
exec(compile(open('core\\Obstacle.py').read(),'core\\Obstacle.py','exec'),globals())
exec(compile(open('core\\Tile.py').read(),'core\\Tile.py','exec'),globals())
exec(compile(open('core\\Block.py').read(),'core\\Block.py','exec'),globals())
exec(compile(open('core\\Structure.py').read(),'core\\Structure.py','exec'),globals())
def getBlock(id:int)-> Block:
    return blockObjs[id]              
def getItem(id:int)-> Item:
    return itemObjs[id]
#for block in blocks:
#    blockObjs.append(Block(block['Id']))
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
def blitInv():
    global craftingGrid,inventory,valid,slothover
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

def blitItems():
    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
    for item in inventory:
        if item['Item'] is not None:
            screen.blit(getItem(item['Item']).sprite,invList[item['Slot']])
            if item['Amount']>1:
                screen.blit(font.render(str(item['Amount']),True,'white'),(invList[item['Slot']][0]-4,invList[item['Slot']][1]+24))
            elif item['Amount']<=0:
                item['Item']=None
    if holdingItem:
        screen.blit(heldItem.sprite,pygame.mouse.get_pos())
        if holdingItem and heldItemAmount>1:
            screen.blit(font.render(str(heldItemAmount),True,'white'),(pygame.mouse.get_pos()[0]-4,pygame.mouse.get_pos()[1]+24))
    slotHover=pygame.Rect(pygame.mouse.get_pos(),(16,16)).collidelist(invRects)
    if slotHover>-1 and inventory[slotHover]['Item']is not None and not holdingItem:
        tBox.update(getItem(inventory[slotHover]['Item']).name)
        tBox.snapToMouse(512)
        tBox.render(screen,True)

while True:
    screen.fill('white')
    currentTile=None
    currentStruct=None
    for tile in tiles:
        if tile.id==player.id:
            currentTile=tile
            obstacles=tile.obstacles
    for structure in structures:
        if structure.id==player.id:
            currentStruct=structure
            if inStruct:
                obstacles=structure.obstacles
    if player.y>512-32 and not inStruct:
        player.y=0
        player.id+=16
        droppedItems.clear()
        print(player.id)
    elif player.y<0 and not inStruct:
        player.y=512-32
        player.id-=16
        droppedItems.clear()
        print(player.id)
    elif player.x>512-32 and not inStruct:
        player.x=0
        player.id+=1
        droppedItems.clear()
        print(player.id)
    elif player.x<0 and not inStruct:
        player.x=512-32
        player.id-=1
        droppedItems.clear()
        print(player.id)
    if mapMode:
        loadLevel(level)
    if not inStruct:
        currentTile.loadTile()
    else:
        currentStruct.loadTile()
        
    currentItem=inventory[selectorPos+17]
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
            if keys[pygame.K_F3]:
                #Reload Classes
                exec(compile(open('core\\Player.py').read(),'core\\Player.py','exec'),globals())
                x,y=player.x,player.y
                player=Player(x,y)
                player.id=currentTile.id
                exec(compile(open('core\\Item.py').read(),'core\\Item.py','exec'),globals())
                itemObjs.clear()
                for item in items:
                    itemObjs.append(Item(item['Id']))
                exec(compile(open('core\\Recipe.py').read(),'core\\Recipe.py','exec'),globals())
                recipeObjs.clear()
                for recipe in recipes:
                    recipeObjs.append(Recipe(recipe['Id']))
                exec(compile(open('core\\Obstacle.py').read(),'core\\Obstacle.py','exec'),globals())
                currentTile.createObstacles()
                exec(compile(open('core\\Tile.py').read(),'core\\Tile.py','exec'),globals())
                #exec(compile(open('core\\Block.py').read(),'core\\Block.py','exec'),globals())
                exec(compile(open('core\\Structure.py').read(),'core\\Structure.py','exec'),globals())
                #for block in blocks:
                #    blockObjs.append(Block(block['Id']))
            if keys[pygame.K_SLASH]:
                print('Commands')
            if keys[pygame.K_e]:
                if smeltOpen:
                    smeltOpen=False
                elif not invOpen:
                    invOpen=True
                elif invOpen:
                    invOpen=False
        currentItem=inventory[selectorPos+17]
        if event.type==pygame.MOUSEBUTTONDOWN and not invOpen and not smeltOpen:
            currentItem=inventory[selectorPos+17]
            mouseRect=pygame.Rect((pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1]),(8,8))
            if currentItem['Item'] is not None and event.dict['button']==1:
                if getItem(currentItem['Item']).type=='Block':
                    #print('ur mom')
                    for block in obstacleData:
                        if block['ParentId']==currentItem['Item']:
                            print(block['ParentId'],currentItem['Item'])
                            print('place')
                            currentBlock=block
                            for i in range(len(obstacles)):
                                obData=obstacles[i].checkCollisionDamage(mouseRect,False,False,False)
                                #print(obData)
                                if obData!=False:
                                    if obData[0]:
                                        #print('ur dad')
                                        oldob=currentTile.obstacles.pop(i)
                                        currentTile.obstacles.insert(i,Obstacle(currentBlock['Id'],oldob.rect,i))
                                        currentTile.obstacles.insert(i,Obstacle(currentBlock['Id'],oldob.rect,i))
                                        #currentTile.obstacles=obstacles.copy()
                                        #for ob in currentTile.obstacles:
                                        #
                                        #    print(ob.sprite)
                                        currentItem['Amount']-=1
                                        if currentItem['Amount']==0:
                                            currentItem['Item']=None
                                        break
                            break
            if event.dict['button']==3:
                for obstacle in obstacles:
                    obData=obstacle.checkCollisionDamage(mouseRect,False,False,False)
                    if obData!=False:
                        if obData[0]:
                            obstacle.interact()                   
            if pygame.mouse.get_pos().__getitem__(0)>player.x and event.dict['button']==1 and currentItem['Item']==8: 
                for frame in range(len(slash)):
                    screen.fill('white')
                    currentTile.loadTile()
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
                    droppedItems.append(ob.checkCollisionDamage(slashRect,True,True,True))
                    droppedItems.append(droppedItems[-1])
            elif event.dict['button']==1 and currentItem['Item']==None: 
                for ob in obstacles:
                    if ob.harvestLevel!=-1:
                        if ob.harvestLevel==0:
                            droppedItems.append(ob.checkCollisionDamage(mouseRect,True,True,True))
            elif event.dict['button']==1 and currentItem['Item']==14:
                random.choice(horns).play()   
            elif pygame.mouse.get_pos().__getitem__(0)<=player.x and event.dict['button']==1 and currentItem['Item']==8:
                for frame in range(len(slashL)):
                    screen.fill('white')
                    currentTile.loadTile()
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
        elif event.type==pygame.MOUSEBUTTONDOWN:
            if invOpen:
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
            elif smeltOpen:
                slotHover=pygame.Rect(pygame.mouse.get_pos(),(16,16)).collidelist(invRects)
                #1 = LMB
                #2 = MMB
                #3 = RMB
                if event.dict['button']==1:
                    #If output clicked
                    if slotHover==33 and inventory[slotHover]['Item']is not None and not holdingItem and valid and slotHover in [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,25,31,33]:
                        holdingItem=True
                        heldItem=getItem(inventory[slotHover]['Item'])
                        heldItemAmount=inventory[slotHover]['Amount']
                        inventory[slotHover]['Item']=None
                        inventory[slotHover]['Amount']=0
                    elif slotHover==33 and holdingItem:
                        pass
                    #If slot with a item clicked empty handed
                    elif slotHover>-1 and inventory[slotHover]['Item']is not None and not holdingItem and slotHover in [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,25,31,33]:
                        holdingItem=True
                        heldItem=getItem(inventory[slotHover]['Item'])
                        heldItemAmount=inventory[slotHover]['Amount']
                        inventory[slotHover]['Item']=None
                        inventory[slotHover]['Amount']=0
                    #1Add item count if possible
                    elif slotHover>-1 and inventory[slotHover]['Item']==heldItem.itemId and holdingItem and inventory[slotHover]['Amount']+heldItemAmount<=heldItem.maxStackSize and slotHover in [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,25,31,33]:
                        holdingItem=False
                        inventory[slotHover]['Amount']+=heldItemAmount
                    #1Switch held item
                    elif slotHover>-1 and inventory[slotHover]['Item']!=heldItem.itemId and inventory[slotHover]['Item']is not None and holdingItem and slotHover in [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,25,31,33]:
                        if slotHover==31:
                            if 'solidFuel' in heldItem.tags:
                                tempItem=heldItem
                                tempItemAmount=heldItemAmount
                                heldItem=getItem(inventory[slotHover]['Item'])
                                heldItemAmount=inventory[slotHover]['Amount']
                                inventory[slotHover]['Item']=tempItem.itemId
                                inventory[slotHover]['Amount']=tempItemAmount
                        else:
                            tempItem=heldItem
                            tempItemAmount=heldItemAmount
                            heldItem=getItem(inventory[slotHover]['Item'])
                            heldItemAmount=inventory[slotHover]['Amount']
                            inventory[slotHover]['Item']=tempItem.itemId
                            inventory[slotHover]['Amount']=tempItemAmount
                        #Drop item if click outside inventory area
                    #1Place item in empty slot
                    elif slotHover>-1 and inventory[slotHover]['Item']is None and holdingItem and inventory[slotHover]['Amount']<=heldItem.maxStackSize and slotHover in [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,25,31,33]:
                        if slotHover==31:
                            if 'solidFuel' in heldItem.tags:
                                holdingItem=False
                                inventory[slotHover]['Item']=heldItem.itemId
                                inventory[slotHover]['Amount']=heldItemAmount
                        else:
                            holdingItem=False
                            inventory[slotHover]['Item']=heldItem.itemId
                            inventory[slotHover]['Amount']=heldItemAmount
                if event.dict['button']==3:
                    if slotHover>-1 and inventory[slotHover]['Item']is not None and not holdingItem and slotHover in [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,25,31,33]:
                        holdingItem=True
                        heldItem=getItem(inventory[slotHover]['Item'])
                        heldItemAmount=1
                        inventory[slotHover]['Amount']-=1
                        if inventory[slotHover]['Amount']<=0:
                            inventory[slotHover]['Item']=None
                    #1Stacking RMB
                    elif slotHover>-1 and inventory[slotHover]['Item']==heldItem.itemId and holdingItem and inventory[slotHover]['Amount']+heldItemAmount<=heldItem.maxStackSize and slotHover in [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,25,31,33]:
                        if slotHover==31:
                            if 'solidFuel' in heldItem.tags:
                                holdingItem=False
                                inventory[slotHover]['Amount']+=heldItemAmount
                        else:
                            holdingItem=False
                            inventory[slotHover]['Amount']+=heldItemAmount
                    #1Place 1 Item in empty slot
                    elif slotHover>-1 and inventory[slotHover]['Item']is None and holdingItem and inventory[slotHover]['Amount']<=heldItem.maxStackSize and slotHover in [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,25,31,33]:
                        if slotHover==31:
                            if 'solidFuel' in heldItem.tags:
                                heldItemAmount-=1
                                if heldItemAmount==0:
                                    holdingItem=False
                                inventory[slotHover]['Item']=heldItem.itemId
                                inventory[slotHover]['Amount']+=1
                        else:
                            heldItemAmount-=1
                            if heldItemAmount==0:
                                holdingItem=False
                            inventory[slotHover]['Item']=heldItem.itemId
                            inventory[slotHover]['Amount']+=1
    mouseRect=pygame.Rect((pygame.mouse.get_pos()[0]-16,pygame.mouse.get_pos()[1]-16),(8,8))
    if currentItem['Item'] is not None:
        if getItem(currentItem['Item']).type=='Block':
            for block in obstacleData:
                if block['ParentId']==currentItem['Item']:
                    currentBlock=block
                    for i in range(len(obstacles)):
                        if obstacles[i].checkCollisionDamage(mouseRect,False,False,False):
                            hover=pygame.image.load(currentBlock['Sprite'])
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
        blitInv()
    elif smeltOpen:
        for command in smeltStuff:
            command()
        if inventory[31]['Item'] is not None and fuel==0:
            fuel+=getItem(inventory[31]['Item']).burnTime
            maxFuel=getItem(inventory[31]['Item']).burnTime
            inventory[31]['Amount']-=1
            if inventory[31]['Amount']<=0:
                inventory[31]['Item']=None
        if inventory[25]['Item'] is not None and fueled:
            for recipe in smeltRecipes:
                if recipe.checkRecipe([inventory[25]['Item']]):
                    threading.Thread(target=smelt).start()
                    smelting=True
                    currentRecipe=recipe
            if smeltDone:  
                smeltDone=False      
                inventory[33]['Item']=currentRecipe.output
                inventory[33]['Amount']=currentRecipe.count
                valid=True
                inventory[25]['Amount']-=1
                if inventory[25]['Amount']==0:
                    inventory[25]['Item']=None
            else:
                inventory[33]['Item']=None
                inventory[33]['Amount']=0
                valid=False
                    
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
    if fuel>0:
        fuel-=1
        if fuel/maxFuel==0:
            currentSmelt=smelt5
            fueled=False
        elif fuel/maxFuel <0.2:
            currentSmelt=smelt4
            fueled=True
        elif fuel/maxFuel <0.4:
            currentSmelt=smelt3
            fueled=True
        elif fuel/maxFuel <0.6:
            currentSmelt=smelt2
            fueled=True
        elif fuel/maxFuel <0.8:
            currentSmelt=smelt1
            fueled=True
        elif fuel/maxFuel <1:
            currentSmelt=smelt0
            fueled=True            
        smeltStuff=[lambda:screen.blit(invOverlay,(0,0)),lambda:screen.blit(invOverlay2,(0,32)),lambda:screen.blit(currentSmelt,(0,0)),lambda:blitItems()]          
    ver.render(screen,True)
    pygame.display.update()
    clock.tick(60)