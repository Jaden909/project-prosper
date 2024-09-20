#import pydub.effects
#import pydub.playback
import pygame,PyEngine,random,time as realTime,ctypes,os,sys,threading,pickle,copy,gc,math,traceback#,pydub
from pathlib import PurePath
from research import research
if sys.platform=='win32':
    ctypes.windll.shcore.SetProcessDpiAwareness(0)
#EXPERIMENTAL SCALING
SCALE=(1,1)
#Determines how broken old saves are: Whole number changes break saves completely, decimal number changes don't include all new game content. Ex: version 1 would completely break version 0 saves, while version 0.1 would only prevent some new content from appearing
saveVersion=0
#SCALE=(2,2)
#SCALE=(3.75,2.109375)
print(f'Window Size: {512*SCALE[0]}x{512*SCALE[1]}')

mainScreen=pygame.display.set_mode((512*SCALE[0],512*SCALE[1]),pygame.RESIZABLE)
screen=pygame.Surface((512,512))
#screen=pygame.display.set_mode((512,512),pygame.RESIZABLE)
pygame.display.set_caption('Project Prosper','idk')
pygame.display.set_icon(pygame.image.load(PurePath('misc','icon.png')))
horn0=pygame.mixer.Sound(PurePath('sfx','horn0.wav'))
horn1=pygame.mixer.Sound(PurePath('sfx','horn1.wav'))
horn2=pygame.mixer.Sound(PurePath('sfx','horn2.wav'))
horn3=pygame.mixer.Sound(PurePath('sfx','horn3.wav'))
horns=[horn0,horn1,horn2,horn3]
pygame.mixer_music.load(PurePath('sfx','test2.wav'))
#pygame.mixer_music.load(PurePath('sfx','gameOver.mid'))
#pygame.mixer_music.play()
#d:pydub.AudioSegment=pydub.AudioSegment.from_wav(PurePath('sfx','horn0.wav'))

#d.speedup(5)
#d.set_frame_rate(2)
#pygame.mixer.Sound(pydub.effects.speedup(d,random.choice(range(90,110))/100).export(format='wav')).play()
#print(type(d))


# NOTES
# bow responds to infinity
# 
# 
# PyEngine 
# 
# 
# PyEngine 
# 
# 
# 
# 
# 
# 

# 

# 
# 
# 

# Item Tool:
# 
# 
# Current limits:
# 
# 

# 
# 
# 
#
#
#
#
#
# TODO: Set mute var to True
# 


#PROBLEMS
# 
# 
# 
# 
# Furnace visual needs fixed

#Future
#Load Game screen
#weather
#sounds/ambience
#Load game screen
#Animate player

#only blit updated areas of screen

#Command Ideas
#/spawn
#/tile- get tile data

#252x28

#Seasonal Events
currentTime=realTime.localtime()
eventActive=False
xmas=False


tiles=[]
#print(currentTime[1],currentTime[2])
if currentTime[1]==12 and currentTime[2]==1:
    eventItems=[14]
    eventActive=True
elif currentTime[1]==12 and currentTime[2] in range(15,26):
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
bossFont=pygame.font.SysFont('gabriola',30,False,True)
chatFont=pygame.font.Font('Coure.fon',10)

fastStart=False
newGameStart=False
gameStarting=False
seed=None
#print(fastStart)
uiQueue=[]
currentRecipe=None
done=False
inStruct=False
chestOpen=False
closeQueue=[]
chestStuff=[]

tilesLoaded=0

cursorChange=False
smeltOpen=False
eventQueue=[]
playerMoved=False
obCache={}

maxSpawnDelay=250
spawnDelay=maxSpawnDelay
spawnChance=20

fuel=0
maxFuel=0
frames=0

startTime=0
newsOpen=False
levelMap=[]
modObjs=[]

footstepDelay=500
footstepStartTime=0
oldPlayerPos=(0,0)
researches=[False for i in range(len(PyEngine.load(PurePath('data','techTree.json'))))]

infinity=True
# Settings 

advancedTooltips=False
mute=True
autosave=True
drawHitboxes=False
debugInv=False
mods=False
scale=(1,1)

if sys.platform=='win32' or sys.platform=='linux' and not hasattr(sys,'getandroidapilevel'):
    controls={'inv':'e','up':'w','down':'s','left':'a','right':'d'}
    mobile=False
elif hasattr(sys,'getandroidapilevel'):
    controls={'inv':'e','up':'w','down':'s','left':'a','right':'d'}
    mobile=True
#mobile=True


#print(pygame.key.key_code('a'))
exec(compile(open(PurePath('core','Obstacle.py')).read(),'Obstacle.py','exec'),globals())
exec(compile(open(PurePath('core','Tile.py')).read(),'Tile.py','exec'),globals())
exec(compile(open(PurePath('core','Structure.py')).read(),'Structure.py','exec'),globals())

newsOverlay=pygame.image.load(PurePath('misc','nightOverlay.png'))
unknown=pygame.image.load(PurePath('items','unknown.png'))
newsOverlay.set_alpha(200)
ver=PyEngine.TextBox('Project Prosper ALPHA (Summer Update)',0,487,25,410,'coure.fon',15,False,False,'black',(251, 182, 104),(155, 82, 0),2,(5,5)) 
#Main Menu______________________________________________________________________________________________________________________________________________________________________________________
def newGameToggle():
    global newGameStart
    newGameStart=True
def options():
    print('No options yet')
def setDistribution(value):
    global distribution
    distribution=value
def startGame():
    global gameStarting,seed,start,newGameToggle,newGame,options,setDistribution,mainMenuOverlay,newGameButt,optionsButt,exitButt,seedEntry,equalButt,oceansButt,balancedButt,createWorldButt
    gameStarting=True
    if seedText!='':
        seed=seedText
    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
    #del newGameToggle,newGame,options,setDistribution,mainMenuOverlay,newGameButt,optionsButt,exitButt,seedEntry,equalButt,oceansButt,balancedButt,createWorldButt
    screen.blit(pygame.transform.scale(pygame.transform.scale(mainMenuImg,(.5,.5)),(2,2)),(0,0))
    screen.blit(font.render('Generating World...',True,'white'),(200,220))
    PyEngine.disableAll()
    pygame.display.update()
    start=realTime.time()
def news():
    global newsOpen
    newsOpen=True
    #print('news')
def notNews():
    global newsOpen
    newsOpen=False
if not fastStart:
    if not xmas:
        mainMenuImg=pygame.image.load(PurePath('misc','menu','mainMenu.png'))
        projectImg=pygame.image.load(PurePath('misc','menu','project.png'))
    else:
        mainMenuImg=pygame.image.load('misc','menu','mainMenuXmas.png')
        projectImg=pygame.image.load('misc','menu','projectXmas.png')
    prosperImg=pygame.image.load(PurePath('misc','menu','prosper.png'))
    mainMenuOverlay=pygame.image.load(PurePath('misc','menu','mainMenuOverlay.png'))
    #mainMenuOverlay.set_alpha(150)
    newGameButt=PyEngine.GameButton(200,325,newGameToggle,'default',True,True,'default',64,PurePath('misc','menu','button.png'),120,40,PurePath('misc','menu','buttonAlt.png'),scale=SCALE)
    optionsButt=PyEngine.GameButton(200,380,options,'default',True,True,'default',64,PurePath('misc','menu','button.png'),120,40,PurePath('misc','menu','buttonAlt.png'),scale=SCALE)
    exitButt=PyEngine.GameButton(200,435,exit,'default',True,True,'default',64,PurePath('misc','menu','button.png'),120,40,PurePath('misc','menu','buttonAlt.png'),scale=SCALE)
    seedEntry=PyEngine.GameButton(200,60,pygame.key.start_text_input,'default',True,False,'ibeam',64,PurePath('misc','menu','button.png'),120,40,None,scale=SCALE)
    equalButt=PyEngine.GameButton(60,150,lambda:setDistribution('equal'),'default',True,False,'default',64,PurePath('misc','menu','button.png'),120,40,PurePath('misc','menu','buttonAlt.png'),scale=SCALE)
    oceansButt=PyEngine.GameButton(200,150,lambda:setDistribution('oceans'),'default',True,False,'default',64,PurePath('misc','menu','button.png'),120,40,PurePath('misc','menu','buttonAlt.png'),scale=SCALE)
    balancedButt=PyEngine.GameButton(340,150,lambda:setDistribution('balanced'),'default',True,False,'default',64,PurePath('misc','menu','button.png'),120,40,PurePath('misc','menu','buttonAlt.png'),scale=SCALE)
    createWorldButt=PyEngine.GameButton(200,315,startGame,'default',True,False,'default',64,PurePath('misc','menu','button.png'),120,40,PurePath('misc','menu','buttonAlt.png'),scale=SCALE)
    newsButt=PyEngine.GameButton(480,480,news,'default',True,True,'default',32,PurePath('misc','menu','news.png'),120,40,PurePath('misc','menu','newsAlt.png'),scale=SCALE)
    exitNewsButt=PyEngine.GameButton(480,0,notNews,'default',True,True,'default',32,PurePath('misc','menu','exit.png'),120,40,PurePath('misc','menu','exitAlt.png'),scale=SCALE)
    line=[] 
    seedText=''
    distribution='balanced'
    while not gameStarting and __name__=='__main__':
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit()
            
            if newGameStart and event.type==pygame.TEXTINPUT:
                if event.dict.get('text') in '0123456789qwertyuiopasdfghjklzxcvbnm':
                    line.append(event.dict.get('text'))
                    seedText=''.join(line)
            if event.type==pygame.KEYDOWN:
                keys=pygame.key.get_pressed()
                if newGameStart:
                    if keys[pygame.K_BACKSPACE] and len(line)>0:
                        line.pop(-1)
                        seedText=''.join(line)
                    elif keys[pygame.K_ESCAPE]:
                        newGameStart=False
                if keys[pygame.K_SPACE]:
                    levelMap=pickle.loads(open(PurePath('saves','auto','BIOMES'),'rb').read())
                    tiles=pickle.loads(open(PurePath('saves','auto','TILES'),'rb').read())
                    structures=pickle.loads(open(PurePath('saves','auto','STRUCTURES'),'rb').read())
                    meta=PyEngine.load(PurePath('saves','auto','meta.json'))
                    if meta['version']<saveVersion:
                        print('WARNING: Loading old save. Not all new content will be availible')
                    elif meta['version']>saveVersion:
                        print('WARNING: Loading new save in old version. THIS IS VERY LIKELY TO CAUSE CRASHES AND SAVE CORRUPTIONS!')
                    #print(levelMap,tiles,structures)
                    #newGameStart=True
                    PyEngine.disableAll()
                    gameStarting=True
        if gameStarting:
            break            
        screen.blit(mainMenuImg,(0,0))
        screen.blit(mainMenuOverlay,(40,10))
        if not newGameStart:
            screen.blit(projectImg,(60,20))
            screen.blit(prosperImg,(60,150))
            PyEngine.disableAll()
            exitButt.enable()
            optionsButt.enable()
            newGameButt.enable()
            newsButt.enable()
        else:
            PyEngine.enableAll()
            exitButt.disable()
            optionsButt.disable()
            newGameButt.disable()
            exitNewsButt.disable()
            newsButt.disable()
            #screen.blit(tipOverlay,(5,360))
        if newsOpen:
            PyEngine.disableAll()
            newGameButt.show(screen)
            optionsButt.show(screen)
            exitButt.show(screen)
            screen.blit(newsOverlay,(0,0))
            exitNewsButt.enable()
            exitNewsButt.show(screen)
            exitNewsButt.listen(screen)   
            i=0
            for line in PyEngine.autoWrap(open(PurePath('misc','news.txt')).read(),480,font,'white',True):
                screen.blit(line,(10,i*25+25))
                i+=1
        PyEngine.showAll(screen)
        PyEngine.listenAll(screen)
        if not newGameStart:
            screen.blit(font.render('New Game',True,'black'),(230,338))
            screen.blit(font.render('Options',True,'black'),(230,393))
            screen.blit(font.render('Exit',True,'black'),(245,448))
        elif not gameStarting and newGameStart: 
            #screen.blit(font.render('New World',True,'black','white'),(225,20))
            PyEngine.TextBox('New World',220,20,20,80,'coure.fon',12,False,False,'black',(228, 155, 73),(155,82,0),2,(5,3)).render(screen)
            screen.blit(font.render('Seed',True,'black'),(245,40))
            screen.blit(font.render(seedText,True,'black'),(215,72))
            screen.blit(font.render(f'Distribution: {distribution}',True,'black'),(180,120))
            screen.blit(font.render(f'Equal',True,'black'),(100,162))
            screen.blit(font.render(f'Oceans',True,'black'),(235,162))
            screen.blit(font.render(f'Balanced',True,'black'),(365,162))
            #Equal Description
            equalText=PyEngine.autoWrap('Equal: All biomes have an equal chance of generating',120,font,'black')
            for i in range(len(equalText)):
                screen.blit(equalText[i],(55,200+i*20))
            oceanText=PyEngine.autoWrap('Oceans: oceans are more likely to appear',120,font,'black')
            for i in range(len(oceanText)):
                screen.blit(oceanText[i],(195,200+i*20))
            balText=PyEngine.autoWrap('Balanced: Biomes balanced for a more balanced playthrough (Recommended)',150,font,'black')
            for i in range(len(balText)):
                screen.blit(balText[i],(335,200+i*20))    
            screen.blit(font.render('Create World',True,'black'),(210,328))    
        
        ver.render(screen)
        mainScreen.blit(pygame.transform.scale(screen,(512*SCALE[0],512*SCALE[1])),(0,0))
        pygame.display.update()



grass=pygame.image.load(PurePath('biomes','grass.png')).convert()
ocean=pygame.image.load(PurePath('biomes','ocean.png')).convert()
desert=pygame.image.load(PurePath('biomes','desert.png')).convert()
forest=pygame.image.load(PurePath('biomes','forest.png')).convert()

slash0=pygame.image.load(PurePath('Slash','slash0.png'))
slash1=pygame.image.load(PurePath('Slash','slash1.png'))
slash2=pygame.image.load(PurePath('Slash','slash2.png'))
slash3=pygame.image.load(PurePath('Slash','slash3.png'))
slash4=pygame.image.load(PurePath('Slash','slash4.png'))
slash5=pygame.image.load(PurePath('Slash','slash5.png'))
slash6=pygame.image.load(PurePath('Slash','slash6.png'))
slash7=pygame.image.load(PurePath('Slash','slash7.png'))

slashFrame=0
slashStartTime=0
slashDone=True
heldItem=None

slashL0=pygame.image.load(PurePath('SlashLeft','slash0.png'))
slashL1=pygame.image.load(PurePath('SlashLeft','slash1.png'))
slashL2=pygame.image.load(PurePath('SlashLeft','slash2.png'))
slashL3=pygame.image.load(PurePath('SlashLeft','slash3.png'))
slashL4=pygame.image.load(PurePath('SlashLeft','slash4.png'))
slashL5=pygame.image.load(PurePath('SlashLeft','slash5.png'))
slashL6=pygame.image.load(PurePath('SlashLeft','slash6.png'))
slashL7=pygame.image.load(PurePath('SlashLeft','slash7.png'))

slashSpeed=50
slashLFrame=0
slashLStartTime=0
slashLDone=True

slash=[slash0,slash1,slash2,slash3,slash4,slash5,slash6,slash7]
slashL=[slashL0,slashL1,slashL2,slashL3,slashL4,slashL5,slashL6,slashL7]

slashAnimation=PyEngine.Animation(slash,slashSpeed)
slashLAnimation=PyEngine.Animation(slashL,slashSpeed)

invOverlay=pygame.image.load(PurePath('objects','invOverlay.png')).convert_alpha()
invOverlay2=pygame.image.load(PurePath('objects','invOverlay2.png')).convert_alpha()
invOverlay3=pygame.image.load(PurePath('objects','craftOverlay.png')).convert_alpha()
hbOverlay=pygame.image.load(PurePath('objects','hotBarOverlay.png')).convert_alpha()
invScreen=pygame.image.load(PurePath('objects','invScreen3.png')).convert_alpha()
chatLine=pygame.image.load(PurePath('misc','ui','chatLineOverlay.png')).convert_alpha()
hotBar=pygame.image.load(PurePath('objects','hotBar.png')).convert_alpha()
hotBarSelector=pygame.image.load(PurePath('objects','hotBarSelector.png')).convert_alpha()
night=pygame.image.load(PurePath('misc','nightOverlay.png')).convert_alpha()
black=pygame.image.load(PurePath('misc','menu','black.png'))
smeltOverlay=pygame.image.load(PurePath('objects','smeltOverlay.png'))

invOverlay.set_alpha(150)
invOverlay2.set_alpha(200)
invOverlay3.set_alpha(200)
hbOverlay.set_alpha(200)
chatLine.set_alpha(200)
night.set_alpha(0)
black.set_alpha(150)

test=pygame.image.load(PurePath('objects','test.png')).convert_alpha()
hbvis=pygame.image.load(PurePath('misc','hb','hitboxVis.png')).convert_alpha()
hbvisBig=pygame.image.load(PurePath('misc','hb','hitboxVisBig.png')).convert_alpha()
hbvisNone=pygame.image.load(PurePath('misc','hb','hitboxVisNone.png')).convert_alpha()
hbvisBigNone=pygame.image.load(PurePath('misc','hb','hitboxVisNoneBig.png')).convert_alpha()
hbvisBigBlock=pygame.image.load(PurePath('misc','hb','hitboxVisBigBlock.png')).convert_alpha()
hbvisBigSolid=pygame.image.load(PurePath('misc','hb','hitboxVisBigSolid.png')).convert_alpha()
hbvisSolid=pygame.image.load(PurePath('misc','hb','hitboxVisSolid.png')).convert_alpha()
bossBar=pygame.image.load(PurePath('misc','ui','bossBar.png')).convert_alpha()
stun=pygame.image.load(PurePath('misc','stun.png')).convert_alpha()

bgCache={'g':pygame.image.load(PurePath('biomes','grass.png')).convert_alpha(),'d':pygame.image.load(PurePath('biomes','desert.png')).convert_alpha(),'f':pygame.image.load(PurePath('biomes','forest.png')).convert_alpha(),'o':pygame.image.load(PurePath('biomes','ocean.png')).convert_alpha()}
obCache={}


#cactus=pygame.image.load('objects','cactus.png')

none64=pygame.image.load(PurePath('misc','none64.png')).convert_alpha()
hungerIcon=pygame.image.load(PurePath('misc','ui','hungerIcon.png')).convert_alpha()
hpIcon=pygame.image.load(PurePath('misc','ui','heartIcon.png')).convert_alpha()
hpUnder=pygame.image.load(PurePath('misc','ui','hpUnder.png')).convert_alpha()
chestOverlay=pygame.image.load(PurePath('objects','chestOverlay.png')).convert_alpha()
chestOverlay.set_alpha(200)
goLeft=False
goRight=False
goUp=False
goDown=False
def left():
    global goLeft
    goLeft=True
def right():
    global goRight
    goRight=True
def up():
    global goUp
    goUp=True
def down():
    global goDown
    goDown=True
if mobile:
    leftButt=PyEngine.GameButton(20,430,left,imageRes=32,image=PurePath('misc','ui','left.png'),hold=True,scale=SCALE)
    rightButt=PyEngine.GameButton(90,430,right,imageRes=32,image=PurePath('misc','ui','right.png'),hold=True,scale=SCALE)
    upButt=PyEngine.GameButton(55,395,up,imageRes=32,image=PurePath('misc','ui','up.png'),hold=True,scale=SCALE)
    downButt=PyEngine.GameButton(55,430,down,imageRes=32,image=PurePath('misc','ui','down.png'),hold=True,scale=SCALE)

selectorPos=1

chatOpen=False
quickGen=True
snapToMouse=False
valid=False
invFull=False
tileRects=[]
craftRects=[]
scriptQueue=[]
obRects=[]
droppedItems=[]
itemObjs=[]
blockObjs=[]
recipeObjs=[]
enemyObjs=[]
enemies=[]
activeEnemies=[]

projectilePools={}
mouseMotion=False
mapMode=False
    
frame=0
fframe=0
currentProjectile='basic'
invOpen=False
holdingItem=False
ram=100
electricity=0
#key: white=naturally generated with no collision ,black=air/none,blue=block,red=naturally generated with collision/enemy
    
ii=0

line1,line2,line3='','',''
time=0
darker,lighter=True,False
playerImg=pygame.image.load(PurePath('biomes','bigPlayer.png'))
playerImgI=pygame.image.load(PurePath('biomes','bigPlayerI.png'))

#Load core object data
recipes=PyEngine.load(PurePath('data','recipes.json'))
items=PyEngine.load(PurePath('data','items.json'))
enemyData=PyEngine.load(PurePath('data','enemies.json'))
blocks=PyEngine.load(PurePath('data','blocks.json'))
obstacleData=PyEngine.load(PurePath('data','obstacles.json'))
commands=PyEngine.load(PurePath('data','commands.json'))
projectiles=PyEngine.load(PurePath('data','projectiles.json'))

for projectile in projectiles:
    projectilePools[projectile['Name']]=[PyEngine.Projectile(projectile['width'],projectile['height'],projectile['speed'],projectile['acceleration'],projectile['lifetime'],projectile['shootMouse'],PurePath(*projectile['sprite']),offset=projectile['offset'],damage=projectile['damage'],accuracy=projectile['accuracy'])for i in range(projectile['poolCount'])]
#print([projectileObjs])
#0-17 Normal slots, 18-23 hotbar slots, 24+ crafting slots,34-36 furnace slots,37-51 chest slots
#Debug Inv
#inventory=[{'Slot':0,'Item':12,'Amount':5},{'Slot':1,'Item':20,'Amount':1},{'Slot':2,'Item':8,'Amount':1},{'Slot':3,'Item':26,'Amount':1},{'Slot':4,'Item':28,'Amount':1},{'Slot':5,'Item':39,'Amount':1},{'Slot':6,'Item':40,'Amount':4},{'Slot':7,'Item':10,'Amount':1},{'Slot':8,'Item':41,'Amount':1},{'Slot':9,'Item':42,'Amount':1},{'Slot':10,'Item':1,'Amount':64},{'Slot':11,'Item':3,'Amount':64},{'Slot':12,'Item':54,'Amount':1},{'Slot':13,'Item':None,'Amount':0},{'Slot':14,'Item':None,'Amount':0},{'Slot':15,'Item':None,'Amount':0},{'Slot':16,'Item':None,'Amount':0},{'Slot':17,'Item':None,'Amount':0},{'Slot':18,'Item':None,'Amount':0},{'Slot':19,'Item':None,'Amount':0},{'Slot':20,'Item':None,'Amount':0},{'Slot':21,'Item':None,'Amount':0},{'Slot':22,'Item':None,'Amount':0},{'Slot':23,'Item':None,'Amount':0},{'Slot':24,'Item':None,'Amount':0},{'Slot':25,'Item':None,'Amount':0},{'Slot':26,'Item':None,'Amount':0},{'Slot':27,'Item':None,'Amount':0},{'Slot':28,'Item':None,'Amount':0},{'Slot':29,'Item':None,'Amount':0},{'Slot':30,'Item':None,'Amount':0},{'Slot':31,'Item':None,'Amount':0},{'Slot':32,'Item':None,'Amount':0},{'Slot':33,'Item':None,'Amount':0},{'Slot':34,'Item':None,'Amount':0},{'Slot':35,'Item':None,'Amount':0},{'Slot':36,'Item':None,'Amount':0},{'Slot': 37, 'Item': None, 'Amount': 0}, {'Slot': 38, 'Item': None, 'Amount': 0}, {'Slot': 39, 'Item': None, 'Amount': 0}, {'Slot': 40, 'Item': None, 'Amount': 0}, {'Slot': 41, 'Item': None, 'Amount': 0}, {'Slot': 42, 'Item': None, 'Amount': 0}, {'Slot': 43, 'Item': None, 'Amount': 0}, {'Slot': 44, 'Item': None, 'Amount': 0}, {'Slot': 45, 'Item': None, 'Amount': 0}, {'Slot': 46, 'Item': None, 'Amount': 0}, {'Slot': 47, 'Item': None, 'Amount': 0}, {'Slot': 48, 'Item': None, 'Amount': 0}, {'Slot': 49, 'Item': None, 'Amount': 0}, {'Slot': 50, 'Item': None, 'Amount': 0}, {'Slot': 51, 'Item': None, 'Amount': 0}]
#Real Inv
inventory=[{'Slot':0,'Item':None,'Amount':0},{'Slot':1,'Item':None,'Amount':0},{'Slot':2,'Item':None,'Amount':0},{'Slot':3,'Item':None,'Amount':0},{'Slot':4,'Item':None,'Amount':0},{'Slot':5,'Item':None,'Amount':0},{'Slot':6,'Item':None,'Amount':0},{'Slot':7,'Item':None,'Amount':0},{'Slot':8,'Item':None,'Amount':0},{'Slot':9,'Item':None,'Amount':0},{'Slot':10,'Item':None,'Amount':0},{'Slot':11,'Item':None,'Amount':0},{'Slot':12,'Item':None,'Amount':0},{'Slot':13,'Item':None,'Amount':0},{'Slot':14,'Item':None,'Amount':0},{'Slot':15,'Item':None,'Amount':0},{'Slot':16,'Item':None,'Amount':0},{'Slot':17,'Item':None,'Amount':0},{'Slot':18,'Item':None,'Amount':0},{'Slot':19,'Item':None,'Amount':0},{'Slot':20,'Item':None,'Amount':0},{'Slot':21,'Item':None,'Amount':0},{'Slot':22,'Item':None,'Amount':0},{'Slot':23,'Item':None,'Amount':0},{'Slot':24,'Item':None,'Amount':0},{'Slot':25,'Item':None,'Amount':0},{'Slot':26,'Item':None,'Amount':0},{'Slot':27,'Item':None,'Amount':0},{'Slot':28,'Item':None,'Amount':0},{'Slot':29,'Item':None,'Amount':0},{'Slot':30,'Item':None,'Amount':0},{'Slot':31,'Item':None,'Amount':0},{'Slot':32,'Item':None,'Amount':0},{'Slot':33,'Item':None,'Amount':0}]
def getSlot(slots):
    global slotHover
    #print(slots)
    hits=[]
    trueHits=[]
    #print(tempInvRects)
    mouseRect=pygame.Rect(0,0,4,4)
    mouseRect.center=(pygame.mouse.get_pos()[0]/SCALE[0],pygame.mouse.get_pos()[1]/SCALE[1])
    for rect in invRects:
        if mouseRect.colliderect(rect):
            hits.append(invRects.index(rect))
    #print(hits)
    for hit in hits:
        if hit in slots:
            trueHits.append(hit)
    #print(trueHits)
    #print(trueHits)
    if len(trueHits)==0:
        slotHover=-1
    elif len(trueHits)==1:
        slotHover=trueHits[0]
    elif len(trueHits)>1:
        for hit in trueHits:
            if hit<18:
                slotHover=max(trueHits)
                return
        #print('Warning: multiple invRects found. Choosing highest slot number')
        slotHover=max(trueHits)


def registerItems(items):
    '''Register a list of items to the game. Returns a list of the Ids the items were assigned'''
    itemIds=[]
    for item in items:
        if item['Type']=='Tool':
            itemIds.append(len(itemObjs))
            itemObjs.append(Tool(len(itemObjs)))    
        else:
            itemIds.append(len(itemObjs))
            itemObjs.append(Item(len(itemObjs)))
    return itemIds


#from modHelper import modItemObjs
#itemObjs.extend(modItemObjs)

def customRound(x,base):
    return base * round(x/base)
clock=pygame.time.Clock()
exec(compile(open(PurePath('core','Player.py')).read(),'Player.py','exec'),globals())
exec(compile(open(PurePath('core','Item.py')).read(),'Item.py','exec'),globals())
exec(compile(open(PurePath('core','Tool.py')).read(),'Tool.py','exec'),globals())
exec(compile(open(PurePath('core','Mod.py')).read(),'Mod.py','exec'),globals())


#Register vanilla items to the game
registerItems(items)

#EXPERIMENTAL
if mods:
    exec(compile(open(PurePath('modhelper.py')).read(),'modhelper.py','exec'),globals())
    for modFolder in os.listdir('mods'):
        for file in os.listdir(PurePath('mods',modFolder)):
            #Execute any python scripts found in mods folder
            if file[-3:]=='.py':
                exec(compile(open(PurePath('mods',modFolder,file)).read(),file,'exec'),globals())



exec(compile(open(PurePath('core','Recipe.py')).read(),'Recipe.py','exec'),globals())
for recipe in recipes:
    recipeObjs.append(Recipe(recipe['Id']))
#exec(compile(open(PurePath('core','Obstacle.py')).read(),'Obstacle.py','exec'),globals())
#exec(compile(open(PurePath('core','Tile.py')).read(),'Tile.py','exec'),globals())
#exec(compile(open('core','Block.py').read(),'core','Block.py','exec'),globals())
#exec(compile(open(PurePath('core','Structure.py')).read(),'Structure.py','exec'),globals())
exec(compile(open(PurePath('core','Enemy.py' )).read(),'Enemy.py','exec'),globals())

playerSpriteSheet=PyEngine.loadSpriteSheet(PurePath('misc','player.png'),32,8)
playerSprites={'down':playerSpriteSheet[0],'up':playerSpriteSheet[1],'left':playerSpriteSheet[2],'right':playerSpriteSheet[3],'downHold':playerSpriteSheet[4],'upHold':playerSpriteSheet[5],'leftHold':playerSpriteSheet[6],'rightHold':playerSpriteSheet[7]}
#playerSprites={'down':pygame.image.load(PurePath('misc','player','playerDown.png')).convert_alpha(),'up':pygame.image.load(PurePath('misc','player','playerUp.png')).convert_alpha(),'left':pygame.image.load(PurePath('misc','player','playerLeft.png')).convert_alpha(),'right':pygame.image.load(PurePath('misc','player','playerRight.png')).convert_alpha(),'downHold':pygame.image.load(PurePath('misc','player','playerHold','playerHoldDown.png')).convert_alpha(),'upHold':pygame.image.load(PurePath('misc','player','playerHold','playerHoldUp.png')).convert_alpha(),'leftHold':pygame.image.load(PurePath('misc','player','playerHold','playerHoldLeft.png')).convert_alpha(),'rightHold':pygame.image.load(PurePath('misc','player','playerHold','playerHoldRight.png')).convert_alpha()}

player1=Player(256,256,100,100,playerSprites)
player1.id=128
for enemy in enemyData:
    enemyObjs.append(Enemy(enemy['Id']))
def saveWorld(name):
    meta={'name':name,'date':f'{currentTime[1]}/{currentTime[2]}','version':saveVersion}
    try:
        os.listdir(PurePath('saves',name))
    except:
        os.mkdir(PurePath('saves',name))
    try:
        open(PurePath('saves',name,'BIOMES'),'wb').write(pickle.dumps(levelMap))
        open(PurePath('saves',name,'TILES'),'wb').write(pickle.dumps(tiles))
        open(PurePath('saves',name,'STRUCTURES'),'wb').write(pickle.dumps(structures))
        PyEngine.save(PurePath('saves',name,'meta.json'),meta)
    except Exception as e:
        print(f'Saving the world to {name} failed. Save file is corrupted.')
        print(e)
def generate():
    global screen,seed,distribution,start,structures,levelMap
    if levelMap:
        return
    tips=PyEngine.load(PurePath('data','tips.json'))
    tip=random.choice(tips)
    tipLines=PyEngine.autoWrap('Tip: '+tip,480,font,'white')
    tipOverlay=pygame.image.load(PurePath('misc','menu','tipOverlay.png'))
    tipOverlay.set_alpha(150)
    print('Starting World Gen...')
    levelMap=[]
    if fastStart:
        distribution='balanced'
        start=realTime.time()
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
                possibilites=['o','o','f','f','g','g','g','d','d','d','d','d']
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
                    structures.append(Structure(choice2,i,3,[2,3,4,5,10,11,12,13,17,18,19,20,21,34,35,36,37]))
                elif choice=='d':
                    choice2=random.choice(['dTemple'])
                    structures.append(Structure(choice2,i,60))
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
                    structures.append(Structure(choice2,i,3,[2,3,4,5,10,11,12,13,17,18,19,20,21,34,35,36,37]))
                elif choice=='d':
                    choice2=random.choice(['dTemple'])
                    structures.append(Structure(choice2,i,60))
                else:
                    structures.append(Structure('none',i))
                levelMap.append(choice)
            elif distribution=='balanced' and not mapMode:
                possibilites=['o','o','o','f','f','g','g','g','d','d','d','d','d','d']
                possibilites.append(choice)
                possibilites.append(choice)
                choice=random.choice(possibilites)
                tiles.append(Tile(x*512,y*512,choice,i))
                #print(f'Tile {i} Created')
                if choice=='g':
                    choice2=random.choice(['cave'])
                    structures.append(Structure(choice2,i,3,[2,3,4,5,10,11,12,13,17,18,19,20,21,34,35,36,37]))
                elif choice=='d':
                    choice2=random.choice(['dTemple'])
                    structures.append(Structure(choice2,i,60))
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
            screen.blit(mainMenuImg,(0,0))
            screen.blit(black,(0,0))
            screen.set_alpha(125)
            progressBar=pygame.surface.Surface((round(tilesLoaded*225/255),32))
            progressBar.fill('green')
            screen.blit(progressBar,(150,400))
            screen.blit(font.render('Generating World...',True,'white'),(200,220))
            screen.blit(font.render(f'Loaded Tile {tilesLoaded} out of 255',True,'white'),(150,450))
            
            for i in range(len(tipLines)):
                screen.blit(tipLines[i],(25,25+i*25))
            mainScreen.blit(pygame.transform.scale(screen,(512*SCALE[0],512*SCALE[1])),(0,0))
            pygame.display.update() 
        #for tile in tiles:
        #    print(sys.getsizeof(tile.obstacles))     
        random.seed()
        print(realTime.time()-start)
        saveWorld('auto')
        #open(PurePath('saves','BIOMES'),'wb').write(pickle.dumps(levelMap))
        #open(PurePath('saves','TILES'),'wb').write(pickle.dumps(tiles))
        #open(PurePath('saves','STURUCTURES'),'wb').write(pickle.dumps(structures))
        #print(pickle.load(open('WORLD','rb')))
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
    #print(sys.getsizeof(tiles[3].obstacles[0].sprite)) 
carryingItem=False
            
def getItem(id:int,offset=0)-> Item:
    try:
        return itemObjs[id+offset]
    except IndexError:
        print(f'ERROR: Attempted to access item with id of {id}, but no item is registered with that id.')
        return itemObjs[0]
    except TypeError:
        print(f'ERROR: Attempted to access item with NONE id, returning unknown item')
        return itemObjs[0]
def invLoop(slots):
    #Use to handle moving items around in the inventory automatically
    #print(slots)
    global slotHover,holdingItem,heldItem,heldItemAmount,invRects
    #tempInvRects=[i for i in invRects if invRects.index(i) in slots]
    hits=[]
    trueHits=[]
    #print(tempInvRects)
    mouseRect=pygame.Rect(0,0,4,4)
    mouseRect.center=(pygame.mouse.get_pos()[0]/SCALE[0],pygame.mouse.get_pos()[1]/SCALE[1])
    for rect in invRects:
        
        
        if mouseRect.colliderect(rect):
            hits.append(invRects.index(rect))
    #print(hits)
    #pygame.draw.rect(screen,'white',pygame.Rect((pygame.mouse.get_pos()[0]/SCALE[0],pygame.mouse.get_pos()[1]/SCALE[1]),(16,16)))
    #pygame.draw.rect(screen,'white',invRects[36],2)
    #print(hits)
    #print(hits)
    for hit in hits:
        if hit in slots:
            trueHits.append(hit)
    
    #print(hits)
    #print(hits)
    if len(trueHits)==0:
        slotHover=-1
    elif len(trueHits)==1:
        slotHover=trueHits[0]
    elif len(trueHits)>1:
        #print('Warning: multiple invRects found. Choosing highest slot number')
        slotHover=max(trueHits)
    #slotHover=pygame.Rect((pygame.mouse.get_pos()[0]/SCALE[0],pygame.mouse.get_pos()[1]/SCALE[1]),(16,16)).collidelist(tempInvRects)
    #1 = LMB
    #2 = MMB
    #3 = RMB
    #print(slots)
    #print(slotHover)
    if event.dict['button']==1:
        #If output clicked
        #print(slotHover,holdingItem,inventory[slotHover]['Amount'])
        if slotHover==33 and inventory[slotHover]['Item']is not None and not holdingItem and valid:
            #print('brih')
            for nothing in inventory[24:33]:
                if nothing['Item']is not None:
                    #print(inventory.index(nothing))
                    removeOne(inventory.index(nothing))
            holdingItem=True
            #print(inventory[slotHover]['Amount'])
            heldItem=getItem(inventory[slotHover]['Item'])
            heldItemAmount=inventory[slotHover]['Amount']
            removeStack(slotHover)
            return
        elif slotHover==33 and holdingItem:
            pass
        if slotHover==36 and inventory[slotHover]['Item']is not None and not holdingItem:
            holdingItem=True
            heldItem=getItem(inventory[slotHover]['Item'])
            heldItemAmount=inventory[slotHover]['Amount']
            removeStack(slotHover)
        elif slotHover==36 and holdingItem:
            pass
        #If slot with a item clicked empty handed
        elif slotHover>-1 and inventory[slotHover]['Item']is not None and not holdingItem and keys[pygame.K_LSHIFT] and slotHover>24:
            #Shift click into inventory from elsewhere
            for slot in inventory[:24]:
                #print(slot,slotHover)
                if slot['Slot']!=slotHover:
                    if slot['Amount']==0 and slot['Item']is None:
                        addStack(slot['Slot'],inventory[slotHover]['Item'],inventory[slotHover]['Amount'])
                        removeStack(slotHover)
                        break
                    elif slot['Item']==inventory[slotHover]['Item']:
                        slot['Amount']+=inventory[slotHover]['Amount']
                        removeStack(slotHover)
                        break
                else:
                    break
        elif slotHover>-1 and inventory[slotHover]['Item']is not None and not holdingItem:
            holdingItem=True
            heldItem,heldItemAmount=removeStack(slotHover)
            #heldItem=getItem(inventory[slotHover]['Item'])
            #heldItemAmount=inventory[slotHover]['Amount']
            #inventory[slotHover]['Item']=None
            #inventory[slotHover]['Amount']=0
        
        #Add item count if possible
        elif slotHover>-1 and inventory[slotHover]['Item']==heldItem.itemId and holdingItem and inventory[slotHover]['Amount']+heldItemAmount<=heldItem.maxStackSize:
            #print('its this')
            holdingItem=False
            inventory[slotHover]['Amount']+=heldItemAmount
        #Switch held item
        elif slotHover>-1 and inventory[slotHover]['Item']!=heldItem.itemId and inventory[slotHover]['Item']is not None and holdingItem:
            #holdingItem=False
            tempItem=heldItem
            tempItemAmount=heldItemAmount
            heldItem,heldItemAmount=removeStack(slotHover)
            #heldItem=getItem(inventory[slotHover]['Item'])
            #heldItemAmount=inventory[slotHover]['Amount']
            addStack(slotHover,tempItem.itemId,tempItemAmount)
            #inventory[slotHover]['Item']=tempItem.itemId
            #inventory[slotHover]['Amount']=tempItemAmount
            #Drop item if click outside inventory area
        #Place item in empty slot
        
        elif slotHover>-1 and inventory[slotHover]['Item']is None and holdingItem and inventory[slotHover]['Amount']<=heldItem.maxStackSize:
            
            #print('bruh')
            if slotHover==35:
                if hasattr(getItem(heldItem.itemId),'burnTime'):
                    #print('its this')
                    holdingItem=False
                    addStack(slotHover,heldItem.itemId,heldItemAmount)
                    syncInvs('furnace')
                    #smeltInv[1]['Item']=heldItem.itemId
                    #smeltInv[1]['Amount']=heldItemAmount
                    #print('SMELT INV MODIFIED')
            elif slotHover==34:
                holdingItem=False
                addStack(slotHover,heldItem.itemId,heldItemAmount)
                syncInvs('furnace')
                #smeltInv[0]['Item']=heldItem.itemId
                #smeltInv[0]['Amount']=heldItemAmount
                #print('SMELT INV MODIFIED')
            elif slotHover in range(37,52):
                holdingItem=False
                addStack(slotHover,heldItem.itemId,heldItemAmount)
                syncInvs('chest')
                #chestInv[slotHover-37]['Item']=heldItem.itemId
                #chestInv[slotHover-37]['Amount']=heldItemAmount
            
            else:
                #print('its this')
                holdingItem=False
                addStack(slotHover,heldItem.itemId,heldItemAmount)
            #inventory[slotHover]['Item']=heldItem.itemId
            #inventory[slotHover]['Amount']=heldItemAmount
    if event.dict['button']==3:
        if slotHover>-1 and inventory[slotHover]['Item']is not None and not holdingItem:
            holdingItem=True
            heldItem,heldItemAmount=removeOne(slotHover)
            #heldItem=getItem(inventory[slotHover]['Item'])
            #heldItemAmount=1
            #inventory[slotHover]['Amount']-=1
            #if inventory[slotHover]['Amount']<=0:
            #    inventory[slotHover]['Item']=None
        elif slotHover>-1 and inventory[slotHover]['Item']==heldItem.itemId and holdingItem and inventory[slotHover]['Amount']+heldItemAmount<=heldItem.maxStackSize:
            holdingItem=False
            inventory[slotHover]['Amount']+=heldItemAmount
        #place 1 in slot
        elif slotHover>-1 and inventory[slotHover]['Item']is None and holdingItem and inventory[slotHover]['Amount']<=heldItem.maxStackSize:
            heldItemAmount-=1
            if heldItemAmount==0:
                holdingItem=False
            if slotHover==35:
                if hasattr(getItem(heldItem.itemId),'burnTime'):
                    #holdingItem=False
                    addOne(slotHover,heldItem.itemId)
                    syncInvs('furnace') 
                    #smeltInv[1]['Item']=heldItem.itemId
                    #smeltInv[1]['Amount']+=1
                    #print('SMELT INV MODIFIED')
            elif slotHover==34:
                #holdingItem=False
                addOne(slotHover,heldItem.itemId)
                syncInvs('furnace')
                #smeltInv[0]['Item']=heldItem.itemId
                #smeltInv[0]['Amount']+=1
                #print('SMELT INV MODIFIED')
            elif slotHover in range(37,52):
                addOne(slotHover,heldItem.itemId)
                syncInvs('chest') 
                #chestInv[slotHover-37]['Item']=heldItem.itemId
                #chestInv[slotHover-37]['Amount']+=1
            else:
                addOne(slotHover,heldItem.itemId)
            #inventory[slotHover]['Item']=heldItem.itemId
            #inventory[slotHover]['Amount']+=1
#Inv Untils
def removeStack(slot:int):
    item=inventory[slot]['Item']
    amount=inventory[slot]['Amount']
    inventory[slot]['Item']=None
    inventory[slot]['Amount']=0
    return (getItem(item),amount)
def removeOne(slot:int):
    #print(slot)
    item=inventory[slot]['Item']
    if item is None:
        return
    inventory[slot]['Amount']-=1
    if inventory[slot]['Amount']==0:
        inventory[slot]['Item']=None
    return (getItem(item),1)
def addOne(slot,item):
    if inventory[slot]['Item']is None:
        inventory[slot]['Item']=item
    if inventory[slot]['Item']==item:
        inventory[slot]['Amount']+=1
def addStack(slot,item,amount):
    if inventory[slot]['Item']is None:
        inventory[slot]['Item']=item
    if inventory[slot]['Item']==item:
        inventory[slot]['Amount']+=amount
def syncInvs(inv,slots=None):
    #Furnace Sync
    print(inv,'smeltInv' in globals())
    global smeltInv,chestInv
    if 'smeltInv' in globals() and inv=='furnace':
        for slot in inventory[34:37]:
            smeltInv[slot['Slot']-34]['Item']=slot['Item']
            smeltInv[slot['Slot']-34]['Amount']=slot['Amount']
    #Chest Sync 
    elif 'chestInv' in globals() and inv=='chest':
        for slot in inventory[37:52]:
            chestInv[slot['Slot']-37]['Item']=slot['Item']
            chestInv[slot['Slot']-37]['Amount']=slot['Amount']
    #Sync "modded" inventories
    else:
        for slot in inventory[slots[0]:slots[1]]:
            inv[slot['Slot']-slots[0]]['Item']=slot['Item']
            inv[slot['Slot']-slots[0]]['Amount']=slot['Amount']
        return inv
def find(id,slots):
    'Find first instance of given item if it is in given slots'
    for slot in inventory:
        #print(slot['Item'])
        if slot['Item']==id and slot['Slot'] in slots:
            return slot
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
tBox=PyEngine.TextBox('Unknown',0,0,32,64,'Coure.fon',25,False,False,'black','grey','black',3,(5,10))
fps=PyEngine.TextBox(f'FPS: {frames}',430,480,30,80,'Coure.fon',25,True,False,'black',(251, 182, 104),(155, 82, 0),2,(5,5))       

def blitInv():
    global craftingGrid,inventory,valid,slothover
    screen.blit(invOverlay,(0,0))
    screen.blit(invOverlay2,(0,32))
    screen.blit(invOverlay3,(300,32))
    screen.blit(invScreen,(0,0))
    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
    if debugInv:
        for slot in invList:
            pygame.draw.rect(screen,'white',pygame.Rect(slot,(32,32)))
        #ii=0
        #xx=8
        #yy=48
        #for i in range(18):
        #    invPositions.append((xx,yy))
        #    xx+=44
        #    if ii>4:
        #        yy+=52
        #        xx=8
        #        ii=0
        #        continue
        #    ii+=1
        #invDict.update(positions=invPositions)
        #print(invDict)
        #PyEngine.save('InvDebug.json',invDict)
    else:
        for item in inventory:
            if item['Item'] is not None:
                try:
                    screen.blit(getItem(item['Item']).sprite,invList[item['Slot']])
                except AttributeError:
                    screen.blit(unknown,invList[item['Slot']])
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
            screen.blit(heldItem.sprite,(pygame.mouse.get_pos()[0]/SCALE[0],pygame.mouse.get_pos()[1]/SCALE[1]))
            if holdingItem and heldItemAmount>1:
                screen.blit(font.render(str(heldItemAmount),True,'white'),(pygame.mouse.get_pos()[0]/SCALE[0]-4,pygame.mouse.get_pos()[1]/SCALE[1]+24))
        #slotHover=pygame.Rect((pygame.mouse.get_pos()[0]/SCALE[0],pygame.mouse.get_pos()[1]/SCALE[1]),(16,16)).collidelist(invRects)
        #print(slotHover)
        if slotHover>-1 and inventory[slotHover]['Item']is not None and not holdingItem:
            tBox.snapToMouse(512,0,SCALE)
            try:
                tBox.update(getItem(inventory[slotHover]['Item']).name,getItem(inventory[slotHover]['Item']).tooltip)
            except AttributeError:
                tBox.update('Unregistered Item',f'Attempted to access item with id of {inventory[slotHover]["Item"]}, but no item is registered with that id.')
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
        screen.blit(heldItem.sprite,(pygame.mouse.get_pos()[0]/SCALE[0],pygame.mouse.get_pos()[1]/SCALE[1]))
        if holdingItem and heldItemAmount>1:
            screen.blit(font.render(str(heldItemAmount),True,'white'),(pygame.mouse.get_pos()[0]/SCALE[0]-4,pygame.mouse.get_pos()[1]/SCALE[1]+24))
    #slotHover=pygame.Rect((pygame.mouse.get_pos()[0]/SCALE[0],pygame.mouse.get_pos()[1]/SCALE[1]),(16,16)).collidelist(invRects)
    #print(slotHover)
    if slotHover>-1 and inventory[slotHover]['Item']is not None and not holdingItem:
        tBox.snapToMouse(512,0,SCALE)
        tBox.update(getItem(inventory[slotHover]['Item']).name,getItem(inventory[slotHover]['Item']).tooltip)
        
        tBox.render(screen,True)
def send(message,system=True):
    global validCommand,commandParts,line1,line2,line3
    if len(message)>0:
        if message[0]=='/':
            commandParts=cText.split()
            #print(commandParts)
            for command in commands:
                if command['Name']==commandParts[0][1:]:
                    exec(compile(open(PurePath('commands',command['Script'])).read(),command['Script'],'exec'),globals())
                    validCommand=True
            if not validCommand:
                print(f'Command: \'{cText[1:]}\' not found')
        elif not system:
            if line1=='':
                line1=f'Player: {message}'
            elif line2=='':
                line2=line1
                line1=f'Player: {message}'
            else:
                line3=line2
                line2=line1
                line1=f'Player: {message}'
            print(f'Player: {message}')
        else:
            if line1=='':
                line1=f'System: {message}'
            elif line2=='':
                line2=line1
                line1=f'System: {message}'
            else:
                line3=line2
                line2=line1
                line1=f'System: {message}'
            print(f'System: {message}')
def advanceTime(speed):
    global time,darker,lighter
    if darker:
        time+=speed
        night.set_alpha(time)
    elif lighter:
        time-=speed
        night.set_alpha(time)
    if time>=200 and darker:
        darker=False
        lighter=True
    elif time<=0 and lighter:
        darker=True
        lighter=False
#pygame.mixer_music.play()
while __name__=='__main__':
    #mx,my=pygame.mouse.get_pos()
    #correctionAngle=270
    #dx, dy = mx - player.playerRect.centerx, player.playerRect.centery - my
    #angle = math.degrees(math.atan2(-dy, dx)) - correctionAngle
    #playerImg2=pygame.transform.rotate(playerImg,-angle)
    currentTile=None
    #if 'smeltInv' in globals():
    #    print(smeltInv)
    currentStruct=None
    for tile in tiles:
        if tile.id==player1.id:
            currentTile=tile
            obstacles=tile.obstacles
    for structure in structures:
        if structure.id==player1.id:
            currentStruct=structure
            if inStruct:
                obstacles=structure.obstacles
    if player1.y>512-32 and not inStruct:
        player1.y=0
        player1.id+=16
        droppedItems.clear()
        #print(player1.id)
    elif player1.y<0 and not inStruct:
        player1.y=512-32
        player1.id-=16
        droppedItems.clear()
        #print(player1.id)
    elif player1.x>512-32 and not inStruct:
        player1.x=0
        player1.id+=1
        droppedItems.clear()
        #print(player1.id)
    elif player1.x<0 and not inStruct:
        player1.x=512-32
        player1.id-=1
        droppedItems.clear()
        #print(player1.id)
    if mapMode:
        loadLevel(level)
    if inStruct:
        #print('sedf')
        screen.fill('white')
        currentStruct.loadTile()
    elif not inStruct and currentTile is not None:
        screen.fill('white')
        currentTile.loadTile()
    if time>150 and spawnDelay<=0:
        if random.choice(range(101))<spawnChance:
            e=random.choice(enemyObjs)
            if currentTile.biome in e.biomes:
                e.spawn()
        spawnDelay=maxSpawnDelay
            #if enemy not in activeEnemies:
            #enemy.spawn()
    if invOpen:
        slots=list(range(34))
    elif smeltOpen:
        slots=list(range(24))
        slots.extend([34,35,36])
    elif chestOpen:
        slots=list(range(24))
        slots.extend([37,38,39,40,41,42,43,44,45,46,47,48,49,50,51])
    elif not uiQueue:
        slots=[]
    
    currentItem=inventory[selectorPos+17]
    currentIndex=selectorPos+17
    keys=pygame.key.get_pressed()
    PyEngine.showAll(screen)
    PyEngine.listenAll(screen)
    oldPlayerPos=(player1.x,player1.y)
    player1.listenInputs()
    #print((player1.x,player1.y),oldPlayerPos)
    if (player1.x,player1.y)==oldPlayerPos:
        playerMoved=False
    else: playerMoved=True
    for enemy in activeEnemies:
        enemy.update() 
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            if autosave:
                saveWorld('auto')
            exit()
        #if chatOpen and event.type==pygame.TEXTINPUT:
        #    #if event.dict.get('text') in '0123456789qwertyuiopasdfghjklzxcvbnm':
        #    print('input')
        #    cLine.append(event.dict.get('text'))
        #    print(cLine)
        #    cText=''.join(cLine)
        if event.type==pygame.MOUSEMOTION:
            mouseMotion=True
        if event.type==pygame.KEYDOWN:
            keys=pygame.key.get_pressed()
            if keys[pygame.K_F5] and mapMode:
                level=generate()
            elif keys[pygame.K_F5] and not mapMode:
                for tile in tiles:
                    if tile.id==player1.id:
                        tile.createObstacles()
                send('Reloaded tile.')
            if keys[pygame.K_F4]:
                if not drawHitboxes:
                    drawHitboxes=True
                    send('Hitboxes enabled.')
                elif drawHitboxes:
                    drawHitboxes=False
                    send('Hitboxes disabled.')
            if keys[pygame.K_F3]:
                for ob in obstacles:

                    print(ob.type)
                #Reload Classes
                #exec(compile(open(PurePath('core','Player.py')).read(),'Player.py','exec'),globals())
                #x,y=player1.x,player1.y
                #player1=Player(x,y)
                #player1.id=currentTile.id
                #exec(compile(open(PurePath('core','Item.py')).read(),'Item.py','exec'),globals())
                #itemObjs.clear()
                #for item in items:
                #    itemObjs.append(Item(item['Id']))
                #exec(compile(open(PurePath('core','Recipe.py')).read(),'Recipe.py','exec'),globals())
                #recipeObjs.clear()
                #for recipe in recipes:
                #    recipeObjs.append(Recipe(recipe['Id']))
                #exec(compile(open(PurePath('core','Obstacle.py')).read(),'Obstacle.py','exec'),globals())
                #currentTile.createObstacles()
                #exec(compile(open(PurePath('core','Tile.py')).read(),'Tile.py','exec'),globals())
                ##exec(compile(open('core','Block.py').read(),'core','Block.py','exec'),globals())
                #exec(compile(open(PurePath('core','Structure.py')).read(),'Structure.py','exec'),globals())
                #for block in blocks:
                #    blockObjs.append(Block(block['Id']))
                pass
            if keys[pygame.K_F2]:
                print(inventory)
            if keys[pygame.K_F1]:
                print(holdingItem,heldItem,heldItemAmount)
            if keys[pygame.K_SLASH] and not chatOpen:
                chatOpen=True
                cLine=[]
                cText=''
                pygame.key.start_text_input()
                #cLine.append('/')
            if keys[pygame.K_BACKSPACE] and chatOpen:
                cLine.pop()
                cText=''.join(cLine)
            if keys[pygame.K_RETURN] and chatOpen:
                chatOpen=False
                validCommand=False
                send(cText,False)
                #commandParts=cText.split()
                #print(commandParts)
            if keys[pygame.K_t] and not chatOpen:
                chatOpen=True
                cLine=[]
                cText=''
                pygame.key.start_text_input()
                
                
                
            if keys[pygame.key.key_code(controls['inv'])] and not chatOpen:
                
                if smeltOpen:
                    smeltOpen=False
                    syncInvs('furnace') 
                    for slot in inventory[34:37]:
                        slot['Item']=None
                        slot['Amount']=0  
                elif chestOpen:
                    chestOpen=False
                    syncInvs('chest') 
                    for slot in inventory[37:52]:
                        slot['Item']=None
                        slot['Amount']=0  
                elif invOpen:
                    invOpen=False
                elif not invOpen and not uiQueue:
                    invOpen=True
                print(closeQueue)
                for command in closeQueue:
                    command()
                
                #uiQueue.clear()
                #eventQueue.clear()
        if chatOpen and event.type==pygame.TEXTINPUT:
            #if event.dict.get('text') in '0123456789qwertyuiopasdfghjklzxcvbnm':
            #print('input')
            if cLine==[] and event.dict.get('text')=='t':
                pass
            else:
                cLine.append(event.dict.get('text'))
            #print(cLine)
            cText=''.join(cLine)
        currentItem=inventory[selectorPos+17]
        currentIndex=selectorPos+17
        if event.type==pygame.MOUSEBUTTONDOWN and not invOpen and not smeltOpen and not chestOpen and not uiQueue:
            currentItem=inventory[selectorPos+17]
            currentIndex=selectorPos+17
            mouseRect=pygame.Rect((pygame.mouse.get_pos()[0]/SCALE[0],pygame.mouse.get_pos()[1]/SCALE[1]),(2,2))
            if currentItem['Item'] is None and event.dict['button']==1:
                #for pool in projectilePools:
                #    if pool==currentProjectile:
                #        for projectile in  projectilePools[pool]:
                #            if not projectile.active:
                #                projectile.spawn((player1.x+16,player1.y+16))
                #                break
                pass

            if currentItem['Item'] is not None and event.dict['button']==1:
                if getItem(currentItem['Item']).type=='Block':
                    #print('ur mom')
                    for block in obstacleData:
                        if block['ParentId']==currentItem['Item']:
                            #print(block['ParentId'],currentItem['Item'])
                            #print('place')
                            currentBlock=block
                            mouseRect.center=(pygame.mouse.get_pos()[0]/SCALE[0],pygame.mouse.get_pos()[1]/SCALE[1])
                            for i in range(len(obstacles)):
                                obData=obstacles[i].checkCollisionDamage(mouseRect,False,False,False)
                                #print(obData)
                                if obData!=False:
                                    if getItem(currentItem['Item']).canBePlaced is not None:
                                        if obstacles[i].id not in getItem(currentItem['Item']).canBePlaced:
                                            continue
                                    if obData[0]:
                                        #print('ur dad')
                                        oldob=currentTile.obstacles.pop(i)
                                        #oldob=currentTile.obstacles.pop(i)
                                        if currentBlock['Id']==22: #IDFK Its special
                                            currentTile.obstacles.insert(i,Obstacle(currentBlock['Id'],oldob.rect,i))
                                        else:
                                            currentTile.obstacles.insert(i,Obstacle(currentBlock['Id'],oldob.rect,i))
                                            currentTile.obstacles.insert(i,Obstacle(currentBlock['Id'],oldob.rect,i))

                                        #currentTile.obstacles.pop(i)
                                        #currentTile.obstacles=obstacles.copy()
                                        #for ob in currentTile.obstacles:
                                        #
                                        #    print(ob.sprite)
                                        removeOne(currentIndex)
                                        break
                            break
                if currentItem['Item']is not None:
                    if getItem(currentItem['Item']).type=='Tool':
                        getItem(currentItem['Item']).lclick()
                        
                        
            if event.dict['button']==3:
                for obstacle in obstacles:
                    obData=obstacle.checkCollisionDamage(mouseRect,False,False,False)
                    if obData!=False:
                        if obData[0]:
                            obstacle.interact()
                            #break
                if currentItem['Item']is not None:
                    if getItem(currentItem['Item']).type=='Tool':
                        getItem(currentItem['Item']).rclick()                   
            if pygame.mouse.get_pos()[0]/SCALE[0]>player1.x and event.dict['button']==1 and currentItem['Item']==8:
                slashAnimation.start(player1.x+20,player1.y)
                slashRect=pygame.rect.Rect(player1.x+20,player1.y,32,32)
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
            elif pygame.mouse.get_pos()[0]/SCALE[0]<=player1.x and event.dict['button']==1 and currentItem['Item']==8:
                slashLAnimation.start(player1.x-23,player1.y)
                slashRect=pygame.rect.Rect(player1.x-23,player1.y,32,32)
                for ob in obstacles:
                    droppedItems.append(ob.checkCollisionDamage(slashRect,True,True,True))
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
                slots=list(range(34))
                invLoop(slots)
            elif smeltOpen:
                slots=list(range(24))
                slots.extend([34,35,36])
                invLoop(slots)  
            elif chestOpen:
                slots=list(range(24))
                slots.extend([37,38,39,40,41,42,43,44,45,46,47,48,49,50,51])
                invLoop(slots) #Something different
            #print(event)
            for command in eventQueue:
                #print(eventQueue)
                command(event)      
    
    #print(inventory)
    mouseRect=pygame.Rect((pygame.mouse.get_pos()[0]/SCALE[0],pygame.mouse.get_pos()[1]/SCALE[1]),(2,2))
    if currentItem['Item'] is not None:
        carryingItem=True
        heldItemm=getItem(currentItem['Item'])
        if heldItemm.type=='Block':
            for block in obstacleData:
                if block['ParentId']==currentItem['Item']:
                    currentBlock=block
                    mouseRect.center=(pygame.mouse.get_pos()[0]/SCALE[0],pygame.mouse.get_pos()[1]/SCALE[1])
                    for i in range(len(obstacles)):
                        if obstacles[i].checkCollisionDamage(mouseRect,False,False,False):
                            #print(getItem(currentItem['Item']).canBePlaced)
                            if getItem(currentItem['Item']).canBePlaced is not None:
                                #print('its not none')
                                if obstacles[i].id not in getItem(currentItem['Item']).canBePlaced:
                                    pass
                                else:
                                    hover=pygame.image.load(PurePath(*currentBlock['Sprite']))
                                    hover.set_alpha(130)
                                    screen.blit(hover,(customRound(mouseRect.centerx-32,64),customRound(mouseRect.centery-32,64)))
                                    pygame.draw.rect(screen,'blue',mouseRect)
                                    break  
                            else:
                                hover=pygame.image.load(PurePath(*currentBlock['Sprite']))
                                hover.set_alpha(130)
                                screen.blit(hover,(customRound(mouseRect.centerx-32,64),customRound(mouseRect.centery-32,64)))
                                break   
        if getItem(currentItem['Item']).holdScript is not None:
            exec(getItem(currentItem['Item']).holdScript,globals())          
    else:
        carryingItem=False
        cursorChange=False
    invDict=PyEngine.load(PurePath('data','InvDebug.json' ))
    invList=invDict['positions']
    craftDict=PyEngine.load(PurePath('data','craftDebug.json'))
    craftList=craftDict['positions']
    hbDict=PyEngine.load(PurePath('data','hotBarDebug.json' ))
    hbList=hbDict['positons']
    invRects=[]
    
    for slot in invList:
        invRects.append(pygame.Rect(slot,(32,32)))
    #for slot in craftList:
    #    invRects.append(pygame.Rect(slot,(32,32)))
    invPositions=[]
    getSlot(slots)
    #print(len(invRects))
    while None in droppedItems:
        droppedItems.remove(None)
    for item in droppedItems:
        if item != True and item !=False:
            if item['Type'] is not None:
                screen.blit(getItem(item['Type']).sprite,(item['Position'].left+32,item['Position'].top+32))
                if player1.playerRect.colliderect(item['Position']) and not invFull:
                    droppedItems.remove(item)
                    #print('ejufe')
                    getItem(item['Type']).pickUp()

    
            #elif not smelting:
            #    inventory[33]['Item']=None
            #    inventory[33]['Amount']=0
            #    valid=False
                    
    #print(slashDone)

        
        #slashFrame,slashStartTime,slashDone=PyEngine.animation(slash,slashSpeed,screen,player1.x+20,player1.y,slashStartTime,slashFrame)
        

   
        
        #slashLFrame,slashLStartTime,slashLDone=PyEngine.animation(slashL,slashSpeed,screen,player1.x-23,player1.y,slashLStartTime,slashLFrame)
        
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

    #for obstacle in obstacles:
    #    if not obstacle.done:
    #        #obstacle.frame,obstacle.startTime,obstacle.done=PyEngine.animation(PyEngine.loadSpriteSheet(PurePath(*obstacle.animation),64,5),100,screen,obstacle.rect.left,obstacle.rect.top,obstacle.startTime,obstacle.frame)
    #        
    #        #if obstacle.done and obstacle.killMe:
    #        #    obstacles.pop(obstacle.posid)
    #        #    obstacles.insert(obstacle.posid,Obstacle('none',obstacle.colisRect,obstacle.posid)) 
    #        pass
    PyEngine.updateAnimations(screen)
    screen.blit(night,(0,0)) 
    hpBar=pygame.Surface((player1.hp if player1.hp>=0 else 0,16))
    hungerBar=pygame.Surface((player1.hunger if player1.hunger>=0 else 0,16))
    hungerBar.fill('orange')
    if player1.hp>50:
        hpBar.fill('green')
    elif player1.hp>20:
        hpBar.fill('yellow')
    else:
        hpBar.fill('red')
    screen.blit(hpIcon,(362,0))
    screen.blit(hpUnder,(398,8))
    screen.blit(hpBar,(400,10))

    screen.blit(hungerIcon,(362,40))
    screen.blit(hpUnder,(398,48))
    screen.blit(hungerBar,(400,50))
    frames+=1
    #print(uiQueue)
    for command in uiQueue:
        command()
    if invOpen:
        blitInv()
    elif smeltOpen:
        for command in smeltStuff:
            command()
        if smeltInv[1]['Item'] is not None and fuel==0:
            fuel+=getItem(smeltInv[1]['Item']).burnTime
            maxFuel=getItem(smeltInv[1]['Item']).burnTime
            removeOne(35)    
        if inventory[34]['Item'] is not None and fueled:
            for recipe in smeltRecipes:
                if recipe.checkRecipe([inventory[34]['Item']]) and not smelting:
                    threading.Thread(target=smelt).start()
                    smelting=True
                    currentRecipe=recipe
            if smeltDone:  
                print('grgrg')
                smeltDone=False      
                inventory[36]['Item']=currentRecipe.output
                inventory[36]['Amount']+=currentRecipe.count
                valid=True
                removeOne(34)
    elif chestOpen:
        for command in chestStuff:
            command()
    elif not uiQueue:
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
        if currentItem['Item'] is not None and not cursorChange:
            #itemText=PyEngine.TextBox(getItem(currentItem['Item']).name,5,60,25,50,'Coure.fon',25,False,False,'black',None,None,0,(0,0),'')
            #itemText.render(screen)
            itemText=font.render(getItem(currentItem['Item']).name,True,'black')
            screen.blit(itemText,(5,60))
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        elif not cursorChange and not scriptQueue:
            pygame.mouse.set_cursor(pygame.cursors.Cursor((16,16),pygame.image.load(PurePath('misc','hand.png'))))
        if drawHitboxes:
            screen.blit(hbvis,player1.playerRect)
            for obstacle in obstacles:
                try:
                    if obstacle.type=='none':
                        screen.blit(hbvisBigNone,obstacle.colisRect)
                    elif obstacle.parentItem is not None:
                        screen.blit(hbvisBigBlock,obstacle.colisRect)
                    elif obstacle.blockMovement:
                        screen.blit(hbvisBigSolid,obstacle.colisRect)
                    else:
                        screen.blit(hbvisBig,obstacle.colisRect)
                except Exception as e:
                    print(e)
            for enemy in enemies:
                screen.blit(hbvisSolid,enemy.rect)
            
            pygame.draw.rect(screen,'green',mouseRect,border_radius=1)
    
    player1.doHunger()
    
    
    if chatOpen:
        #print(cText)
        #Typing Line
        screen.blit(chatLine,(0,460))
        screen.blit(chatFont.render(cText,True,'white'),(0,460))
        #Line 1
        screen.blit(chatLine,(0,444))
        screen.blit(chatFont.render(line1,True,'white'),(0,444))
        #Line 2
        screen.blit(chatLine,(0,428))
        screen.blit(chatFont.render(line2,True,'white'),(0,428))
        #Line 3
        screen.blit(chatLine,(0,412))
        screen.blit(chatFont.render(line3,True,'white'),(0,412))
    if pygame.time.get_ticks()-startTime>=1000:
        fps.update(f'FPS: {frames}')
        frames=0
        advanceTime(1)
        startTime=pygame.time.get_ticks()
    if pygame.time.get_ticks()-footstepStartTime>=footstepDelay:

        
        if currentTile.sounds is not None and playerMoved and not mute:
            footstepStartTime=pygame.time.get_ticks()
            pygame.mixer.Sound(pydub.effects.speedup(pydub.audio_segment.AudioSegment.from_wav(PurePath('sfx','tiles',currentTile.biome,'footstep',random.choice(currentTile.sounds['footsteps']))),random.choice(range(100,120))/100).export(format='wav')).play()
            
    spawnDelay-=1
    for projectilee in PyEngine.getProjectiles():
        hit=projectilee.update(screen,[enemy.rect for enemy in activeEnemies])
        #print(hit)
        if hit!=-1 and hit is not None:
            activeEnemies[hit].damage(projectilePools[currentProjectile][0].damage)
    #try:

    cursorChange=True
    for command in scriptQueue:
        command()
    #except Exception as e:
    #    print(f'An error occured running something in the script queue. The error was: {e}')
    #scriptQueue.clear()

    ver.render(screen)
    fps.render(screen)  
    #screen.blit(playerImg2,(player.x,player.y))
    
    #snp=tracemalloc.take_snapshot()
    #top_stats = snp.statistics('lineno')
#
    #print("[ Top 10 ]")
    #for stat in top_stats[:10]:
    #    print(stat)

    #screen.blit(testSprites[0],(0,0))
    #screen.blit(testSprites[1],(20,0))
    #screen.blit(testSprites[2],(40,0))
    #screen.blit(testSprites[3],(60,0))
    
    #print(len(PyEngine.getProjectiles()))
    #idk=pygame.image.load(PurePath('boss','boss1','boss1.png'))
    #idk.fill('black')
    #screen.blit(idk,(player.x,player.y))
    #pygame.draw.rect(screen,'red',pygame.Rect((pygame.mouse.get_pos()[0]/SCALE[0],pygame.mouse.get_pos()[1]/SCALE[1]),(4,4)))
    #pygame.draw.line(screen,'green',mouseRect.topleft,mouseRect.topleft)
    size=pygame.display.get_window_size()
    SCALE=(size[0]/512,size[1]/512)
    PyEngine.scale=SCALE
    mainScreen.fill('black')
    if SCALE !=(1,1):  
        mainScreen.blit(pygame.transform.scale(screen,(512*SCALE[0],512*SCALE[1])),(0,0))
    else:
        mainScreen.blit(screen,(0,0))
    #print('bruh')
    #print(inStruct)
    #print(PyEngine.liveProjectiles)
    pygame.display.update() 
    #gc.collect()   
    clock.tick(120)


    