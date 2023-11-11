class Structure:
    def __init__(self,type,id,escape=None,safeZone=None):
        self.type=type
        self.obRects=[]
        self.escape=escape
        if safeZone is not None:
            self.safeZone=safeZone
        else:
            self.safeZone=[]
        #Append new tiles with the cave biome and bind them to the entrances
        if self.type=='cave':
            self.color=pygame.image.load('biomes\\cave.png')
        #elif self.biome=='f':
        #    self.color=pygame.image.load('biomes\\forest.png')
        #elif self.biome=='d':
        #    self.color=pygame.image.load('biomes\\desert.png')
        #elif self.biome=='o':
        #    self.color=pygame.image.load('biomes\\ocean.png')  
        self.id=id
        #self.tileRect=pygame.Rect(self.x,self.y,512,512)
        #tileRects.append(self.tileRect)
        self.obstacles=[]
        self.createObstacles()
    def createObstacles(self):
        global seed
        self.obstacles=[]
        if self.type=='cave':
            x=0
            y=0
            for i in range(256):
                type=random.choice(['none','none','none','caveWall','stone','caveWall','caveWall','stone','caveWall','none'])
                if i in self.safeZone:
                    type='none'
                if i==self.escape:
                    type='escape'
                if type=='stone':
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