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

            self.color=pygame.image.load(PurePath('biomes','cave.png'))
        elif self.type=='dTemple':
            self.color=pygame.image.load(PurePath('biomes','dTemple.png'))
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
            for i in range(64):
                type=random.choice(['none','none','none',6,2,6,7,2,8,'none','none','none',9])
                if i in self.safeZone:
                    type='none'
                if i==self.escape:
                    type='escape'
                self.obstacles.append(Obstacle(type,pygame.rect.Rect((x*64,y*64),(64,64)),i))
                if x==7:
                    y+=1
                    x=0
                    if y==8:
                        break
                    continue 
                x+=1
        elif self.type=='dTemple':
            x=0
            y=0
            for i in range(64):
                type='none'
                if i==self.escape:
                    type='escape'
                if i==4:
                    type=16
                self.obstacles.append(Obstacle(type,pygame.rect.Rect((x*64,y*64),(64,64)),i))
                #self.obstacles.append(Obstacle(type,pygame.rect.Rect((x*64,y*64),(64,64)),i))
                if x==7:
                    y+=1
                    x=0
                    if y==8:
                        break
                    continue 
                x+=1 
            #for obstacle in self.obstacles:
            #    if obstacle.type!='none':
            #        print(obstacle.type)
            #print((self.obstacles))
    def loadTile(self):
        screen.blit(self.color,(0,0))
        for obstaclee in self.obstacles:
            if obstaclee.type != 'none':
                screen.blit(obstaclee.sprite,obstaclee.rect)
                print('fghjk')
        for obstacle in self.obstacles:
                if obstacle.type!='none':
                    print(obstacle.type)      
    def getObstacles(self):
        return self.obstacles