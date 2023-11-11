import pygame,PyEngine,random 
screen=pygame.display.set_mode((512,512))
#level0=pygame.image.load('levelPlan.png')
#level1=pygame.image.load('levelPlan.png')

grass=pygame.image.load('biomes\\grass.png')
ocean=pygame.image.load('biomes\\ocean.png')
desert=pygame.image.load('biomes\\desert.png')
forest=pygame.image.load('biomes\\forest.png')
quickGen=True
tileRects=[]
tiles=[]
mapMode=True
#seedOverride=True
#air=pygame.image.load('air.png')
playerImg=pygame.image.load('biomes\\player.png')


#Rvalue=0
#enemies=[]
#tiles=[]


clock=pygame.time.Clock()
#seed=random.choice(range(1000000,10000000))
class Player:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.currentBiome='unknown'
        self.playerRect=pygame.rect.Rect(self.x,self.y,8,8)
        #self.frames=50
        #self.jumping=False
    def listenInputs(self):
            keys=pygame.key.get_pressed()
            
            #print('fhbvdgh')
            if keys[pygame.K_d]:
                self.x+=1
                screen.blit(playerImg,(self.x,self.y))
            if keys[pygame.K_a]:
                self.x-=1
                screen.blit(playerImg,(self.x,self.y))
            screen.blit(playerImg,(self.x,self.y))
            if keys[pygame.K_w]:
                self.y-=1
                screen.blit(playerImg,(self.x,self.y))
            if keys[pygame.K_s]:
                self.y+=1
                screen.blit(playerImg,(self.x,self.y))
            self.playerRect=pygame.rect.Rect(self.x,self.y,8,8)
            
            #if self.jumping:
            #    if self.frames>0:
            #        self.y-=2
            #        self.frames-=1
            #    elif self.frames<0:
            #        self.y+=1
            #        self.frames-=1
            #    if self.frames==0:
            #        self.frames=-2
            #    elif self.frames==-51:
            #        self.frames=50
            #        self.jumping=False
            #    screen.blit(playerImg,(self.x,self.y))
    #def checkCollisions(self):
    #    #print(tileRects)
    #    global goalRect,leaving
    #    self.playerRect=pygame.Rect(self.x,self.y,32,32)
    #    #print(self.playerRect.collidelist(tileRects))
    #    #Check if player rect is lower to prevent tping up
    #    collision=self.playerRect.collidelist(tileRects)
    #    if collision!=-1:
    #        self.currentBiome=collision
    #        self.y-=2
        
    pygame.display.update()
def generate():
    levelMap=[]
    #Seed Override
    seed=None
    if not quickGen:
        seed=input('Seed:')
    if seed is None:
        seed=random.choice(range(10**18,10**18*10))
        random.seed(seed)
        print(f'Seed: {seed}')
    else:
        if seed=='survival island' or seed=='123':
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
        
            return levelMap
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
    distribution='balanced'

    possibilites=[]
    choice='o'
    x=0
    y=0
    for i in range(256):
        if distribution=='equal':
            possibilites=['o','f','g','d']
            possibilites.append(choice)
            possibilites.append(choice)
            choice=random.choice(possibilites)
            tiles.append(Tile(x*32,y*32,choice,i))
            levelMap.append(choice)
        elif distribution=='oceans':
            possibilites=['o','o','o','f','g','d']
            possibilites.append(choice)
            possibilites.append(choice)
            choice=random.choice(possibilites)
            tiles.append(Tile(x*32,y*32,choice,i))
            levelMap.append(choice)
        elif distribution=='balanced':
            possibilites=['o','o','o','f','f','g','g','g','d']
            possibilites.append(choice)
            possibilites.append(choice)
            choice=random.choice(possibilites)
            tiles.append(Tile(x*32,y*32,choice,i))
            levelMap.append(choice)
        if x==15:
            y+=1
            x=0
            if y==16:
                break 
            continue 
        x+=1      
    random.seed()
    return levelMap


class Tile:
    def __init__(self,x,y,biome,id):
        self.x=x
        self.y=y
        self.biome=biome
        self.id=id
        self.tileRect=pygame.Rect(self.x,self.y,32,32)
        tileRects.append(self.tileRect)
    def checkCollisions(self):
        #print(tileRects)
        #print(self.playerRect.collidelist(tileRects))
        if player.playerRect.colliderect(self.tileRect):
            player.currentBiome=self.biome
            print(f'Current Biome: {player.currentBiome}')
            print(f'id: {self.id}')
            return True
            #print('god help me')
        else:
            return False

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
        #if i=='w':
        #    pass
        if x==15:
            y+=1
            x=0
            if y==16:
                break 
            continue
        x+=1
level=generate()
player=Player(256,256)
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
        if event.type==pygame.KEYDOWN:
            keys=pygame.key.get_pressed()
            if keys[pygame.K_F5]:
                level=generate()
    for i in tiles:
        if i.checkCollisions():
            break
        #print(i.biome)
    #print(level)
    if not mapMode:
        loadLevel(level)
    player.listenInputs()
    pygame.display.update()
    clock.tick(60)
