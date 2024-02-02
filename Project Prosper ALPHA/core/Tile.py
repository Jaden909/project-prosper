class Tile:
    def __init__(self,x,y,biome,id):
        self.x=x
        self.y=y
        self.biome=biome
        self.obRects=[]
        #Append new tiles with the cave biome and bind them to the entrances
        if self.biome=='g':
                self.color=pygame.image.load(PurePath('biomes','grass.png'))

        elif self.biome=='f':
            self.color=pygame.image.load(PurePath('biomes','forest.png'))
        elif self.biome=='d':
            self.color=pygame.image.load(PurePath('biomes','desert.png'))
        elif self.biome=='o':
            if not xmas:
                self.color=pygame.image.load(PurePath('biomes','ocean.png'))
            else:
                self.color=pygame.image.load(PurePath('biomes','snow.png'))

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
        #print(f'Tile {self.id}: Starting obstacles creation')
        global seed,tilesLoaded
        self.obstacles=[]
        self.structure=None
        if self.biome=='g':
            x=0
            y=0
            possibilities=['none','none','none',1,'none','none','none',3,'none','none']
            for i in range(64):
                type=random.choice(possibilities)
                if type==1:
                    self.obstacles.append(Obstacle(type,pygame.rect.Rect((x*64-20,y*64),(64,64)),i))
                else:
                    self.obstacles.append(Obstacle(type,pygame.rect.Rect((x*64,y*64),(64,64)),i))
                if x==7:
                    y+=1
                    x=0
                    if y==8:
                        break
                    continue 
                x+=1
            z=random.choice(range(64)) 
            w=self.obstacles.pop(z)
            self.obstacles.insert(z,Obstacle(5,w.rect,i))
            self.obstacles.insert(z,Obstacle(5,w.rect,i))
            #for ob in self.obstacles:
            #    print(ob.type)
            #print(self.obstacles)
        elif self.biome=='f':
            x=0
            y=0
            for i in range(64):
                type=random.choice(['none',1,3])
                if type==1:
                    self.obstacles.append(Obstacle(type,pygame.rect.Rect((x*64-20,y*64),(64,64)),i))
                else:
                    self.obstacles.append(Obstacle(type,pygame.rect.Rect((x*64,y*64),(64,64)),i))
                if x==7:
                    y+=1
                    x=0
                    if y==8:
                        break
                    continue 
                x+=1 
        elif self.biome=='o':
            x=0
            y=0
            if not xmas:
                possibilities=['none']
            else:
                possibilities=['none','none','none','none','none','none',12,13,14,15,13,13]
            for i in range(64):
                type=random.choice(possibilities)
                if type=='tree':
                    dropsItem=1
                elif type=='stone':
                    dropsItem=3
                else:
                    dropsItem=0
                self.obstacles.append(Obstacle(type,pygame.rect.Rect((x*64,y*64),(64,64)),i))
                if x==7:
                    y+=1
                    x=0
                    if y==8:
                        break
                    continue 
                x+=1
                 
        elif self.biome=='d':
            x=0
            y=0
            for i in range(64):
                type=random.choice(['none','none',4,18])
                if type=='tree':
                    dropsItem=1
                elif type=='stone':
                    dropsItem=3
                else:
                    dropsItem=0
                self.obstacles.append(Obstacle(type,pygame.rect.Rect((x*64,y*64),(64,64)),i))
                if x==7:
                    y+=1
                    x=0
                    if y==8:
                        break
                    continue 
                x+=1
            z=random.choice(range(64)) 
            w=self.obstacles.pop(z)
            self.obstacles.insert(z,Obstacle(17,w.rect,i))
            self.obstacles.insert(z,Obstacle(17,w.rect,i))
        tilesLoaded+=1 
        #print(f'Tile {self.id}: finished obstacle creation')
    def loadTile(self):
        global obRects
        screen.blit(self.color,(0,0))
        for obstaclee in self.obstacles:
            if obstaclee.type != 'none' and not obstaclee.killMe:
                screen.blit(obstaclee.sprite,obstaclee.rect)     
    def getObstacles(self):
        return self.obstacles