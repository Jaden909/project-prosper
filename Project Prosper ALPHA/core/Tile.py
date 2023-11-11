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
        self.structure=None
        if self.biome=='g':
            x=0
            y=0
            possibilities=['none','none','none','tree','mine','none','none','bush','none','none']
            for i in range(256):
                self.isEntrance=False
                type=random.choice(possibilities)

                if type=='tree':
                    dropsItem=1
                elif type=='stone':
                    dropsItem=3
                elif type=='bush':
                    dropsItem=5
                elif type=='mine':
                    possibilities.remove('mine')
                    dropsItem=None
                    self.structure=i
                    self.isEntrance=True
                else:
                    dropsItem=0
                if type=='tree':
                    self.obstacles.append(Obstacle(type,pygame.rect.Rect((x*64-20,y*64),(64,64)),i,dropsItem))
                else:
                    self.obstacles.append(Obstacle(type,pygame.rect.Rect((x*64,y*64),(64,64)),i,dropsItem,self.isEntrance))
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
    def loadTile(self):
        global obRects
        screen.blit(self.color,(0,0))
        for obstaclee in self.obstacles:
            if obstaclee.type != 'none':
                screen.blit(placedObjects[obstaclee.type],obstaclee.rect)     
    def getObstacles(self):
        return self.obstacles