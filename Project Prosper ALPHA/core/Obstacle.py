class Obstacle:
    def __init__(self,id,rect,posid) -> None:
        if id!='none' and id!='escape':
            self.id=id
            self.data=obstacleData[id]
            self.type=self.data['Type']
            
            self.parentItem=self.data['ParentId']
            self.dropsItem=self.data['DropsItem']
            self.isEntrance=self.data['IsEntrance']
            self.scriptFile=self.data['Script']
            # print(self.scriptFile)
            self.blockMovement=self.data['BlockMovement']
            self.sprite=PurePath(*self.data['Sprite'])
            
            try:
                obCache[self.type]
            except KeyError:
                image=pygame.Surface((64,64))
                image.fill((254,0,0))
                image.set_colorkey((254,0,0))
                image.set_clip(None)
                if self.type!='tree':
                    image.blit(pygame.image.load(self.sprite).convert_alpha(),(0,0))
                else:
                    image.blit(pygame.image.load(self.sprite).convert_alpha(),(-15,0))
                obCache[self.type]=image
            #print(self.data['Data'])
            self.obData=copy.deepcopy(self.data['Data'])
            #print(sys.getsizeof(self.sprite))  
            self.harvestLevel=self.data['HarvestLevel']
            if self.data['Animation'] is not None:
                self.animation=self.data['Animation']
            else:
                self.animation=None
            self.frame=0
            self.startTime=0
            self.done=True
        elif id=='none':
            self.type='none'
            self.id='none'
            self.dropsItem=None
            self.isEntrance=None
            self.scriptFile=None
            self.sprite=None
            self.animation=None
            self.harvestLevel=-1
            self.parentItem=None
            self.blockMovement=False
            self.frame=0
            self.startTime=0
            self.done=True
            self.obData=None
        elif id=='escape':
            self.data=obstacleData[0]
            self.type=self.data['Type']
            self.dropsItem=self.data['DropsItem']
            self.isEntrance=self.data['IsEntrance']
            self.scriptFile=self.data['Script']
            self.sprite=PurePath(*self.data['Sprite'])
            self.animation=None
            self.harvestLevel=self.data['HarvestLevel']
            self.blockMovement=False
            self.parentItem=None
            self.frame=0
            self.startTime=0
            self.done=True
            self.obData=None
        if self.scriptFile is not None:
            with open(PurePath('scripts',self.scriptFile)) as script:
                #print('reading script')
                self.script=script.read()
                #print(self.script)

         
        else:
            #print(f'{self.id} GOT SET TO NONE')
            self.script=None
        self.posid=posid
        if self.type=='tree':
            if rect.left>=20:
                self.colisRect=pygame.rect.Rect(rect.left+20,rect.top,rect.width,rect.height)
            else:
                self.colisRect=pygame.rect.Rect(0,rect.top,rect.width,rect.height)
            self.rect=rect
        else:
            self.rect=rect
            self.colisRect=rect
        self.killMe=False
    def checkCollisionDamage(self,rect,doAnimation,getLocation,destorySelf):
        if self.colisRect.colliderect(rect) and not self.killMe:
            

            if destorySelf and not inStruct:
                for tile in tiles:
                    if tile.id==player1.id:
                        #print(self.id)
                        tile.obstacles.pop(self.posid)
                        tile.obstacles.insert(self.posid,Obstacle('none',self.colisRect,self.posid)) 
                        #self.killMe=True
            if destorySelf and inStruct:
                for structure in structures:
                    if structure.id==player1.id:
                        #print(self.id)
                        structure.obstacles.pop(self.posid)
                        structure.obstacles.insert(self.posid,Obstacle('none',self.colisRect,self.posid)) 
                        #self.killMe=True
            if doAnimation and self.animation is not None and destorySelf:  
                PyEngine.Animation(PyEngine.loadSpriteSheet(PurePath(*self.animation),80 if self.type=='tree' else 64,5),100).start(self.rect.left,self.rect.top)
                self.killMe=True
                return {'Type':self.dropsItem,'Position':self.rect}
            if getLocation:
                #print(self.dropsItem)
                if eventActive:
                    if random.randint(0,10)==0:
                        return {'Type':random.choice(eventItems),'Position':self.rect}
                return {'Type':self.dropsItem,'Position':self.rect}
            return True,self.type
        return False
    def interact(self):
        #print('inr')
        #print(self.type)
        global entrancePos,cOb
        cOb=self
        if self.isEntrance:
            entrancePos=(self.rect)
        #print(self.script)
        if self.script is not None:
            #print('exec')
            exec(compile(self.script,self.scriptFile,'exec'),globals())
    def loadSprites(self):
        if self.type!='none':
            try:
                obCache[self.type]
            except KeyError:
                image=pygame.Surface((64,64))
                image.fill((254,0,0))
                image.set_colorkey((254,0,0))
                image.set_clip(None)
                #print(self.sprite)
                if self.type!='tree':
                    image.blit(pygame.image.load(self.sprite).convert_alpha(),(0,0))
                else:
                    image.blit(pygame.image.load(self.sprite).convert_alpha(),(-15,0))
                obCache[self.type]=image
