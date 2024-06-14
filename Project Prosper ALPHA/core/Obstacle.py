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
            self.blockMovement=self.data['BlockMovement']
            self.sprite=PurePath(*self.data['Sprite'])
            try:
                obCache[self.type]
            except KeyError:
                obCache[self.type]=pygame.image.load(self.sprite).convert_alpha()
            #print(self.data['Data'])
            self.obData=copy.deepcopy(self.data['Data'])
            #print(sys.getsizeof(self.sprite))  
            self.harvestLevel=self.data['HarvestLevel']
            if self.data['Animation'] is not None:
                for root, dirs, files in os.walk(PurePath(*self.data["Animation"])):
                    for name in dirs:
                        self.sprites=os.listdir(PurePath(*self.data['Animation'],name))
                self.animation=[]
                for sprite in self.sprites:
                    self.animation.append(PurePath(*self.data['Animation'],name,sprite))
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
                self.script=script.read()

         
        else:
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
            if doAnimation and self.animation is not None and destorySelf:  
                self.done=False
                self.killMe=True
                return {'Type':self.dropsItem,'Position':self.rect}
                #PyEngine.animation(tree,8,5,screen,self.rect.left,self.rect.top)
            if destorySelf and not inStruct:
                for tile in tiles:
                    if tile.id==player1.id:
                        #print(self.id)
                        tile.obstacles.pop(self.posid)
                        tile.obstacles.insert(self.posid,Obstacle('none',self.colisRect,self.posid)) 
                        #self.killMe=True
            elif destorySelf:
                for structure in structures:
                    if structure.id==player1.id:
                        #print(self.id)
                        structure.obstacles.pop(self.posid)
                        structure.obstacles.insert(self.posid,Obstacle('none',self.colisRect,self.posid)) 
                        #self.killMe=True
            if getLocation:
                #print(self.dropsItem)
                if eventActive:
                    if random.randint(0,10)==0:
                        return {'Type':random.choice(eventItems),'Position':self.rect}
                return {'Type':self.dropsItem,'Position':self.rect}
            return True,self.type
        return False
    def interact(self):
        global entrancePos,cOb
        cOb=self
        if self.isEntrance:
            entrancePos=(self.rect)
        if self.script is not None:
            exec(compile(self.script,self.scriptFile,'exec'),globals())
