class Obstacle:
    def __init__(self,id,rect,posid) -> None:
        global obCache
        if id!='none' and id!='escape':
            self.id=id
            self.data=obstacleData[id]
            self.type=self.data['Type']
            
            self.parentItem=self.data['ParentId']
            self.dropsItem=self.data['DropsItem']
            self.isEntrance=self.data['IsEntrance']
            self.scriptFile=self.data['Script']
            if self.data['Sprite']in obCache.keys():
                self.sprite=obCache[self.data['Sprite']] 
            else:
                self.sprite=pygame.image.load(self.data['Sprite'])
                obCache[self.data['Sprite']]=self.sprite
            #print(sys.getsizeof(self.sprite))  
            self.harvestLevel=self.data['HarvestLevel']
            if self.data['Animation'] is not None:
                for root, dirs, files in os.walk(f'{self.data["Animation"]}'):
                    for name in dirs:
                        if sys.platform=='win32':
                            self.sprites=os.listdir(self.data['Animation']+'\\'+name)
                        elif sys.platform=='linux':
                            self.sprites=os.listdir(self.data['Animation']+'/'+name)
                self.animation=[]
                if sys.platform=='win32':
                    for sprite in self.sprites:
                        self.animation.append(pygame.image.load(self.data['Animation']+'\\'+name+'\\'+sprite))
                elif sys.platform=='linux':
                    for sprite in self.sprites:
                        self.animation.append(pygame.image.load(self.data['Animation']+'/'+name+'/'+sprite))
            else:
                self.animation=None
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
        elif id=='escape':
            self.data=obstacleData[0]
            self.type=self.data['Type']
            self.dropsItem=self.data['DropsItem']
            self.isEntrance=self.data['IsEntrance']
            self.scriptFile=self.data['Script']
            self.sprite=pygame.image.load(self.data['Sprite'])
            self.animation=None
            self.harvestLevel=self.data['HarvestLevel']
        if self.scriptFile is not None:
            if sys.platform=='win32':
                self.script=compile(open(f'scripts\\{self.scriptFile}').read(),self.scriptFile,'exec')
            elif sys.platform=='linux':
                self.script=compile(open(f'scripts/{self.scriptFile}').read(),self.scriptFile,'exec')
         
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
    def checkCollisionDamage(self,rect,doAnimation,getLocation,destorySelf):
        if self.colisRect.colliderect(rect):
            
                #PyEngine.animation(tree,8,5,screen,self.rect.left,self.rect.top)
            if destorySelf and not inStruct:
                for tile in tiles:
                    if tile.id==player.id:
                        #print(self.id)
                        tile.obstacles.pop(self.posid)
                        tile.obstacles.insert(self.posid,Obstacle('none',self.colisRect,self.posid)) 
            elif destorySelf:
                for structure in structures:
                    if structure.id==player.id:
                        #print(self.id)
                        structure.obstacles.pop(self.posid)
                        structure.obstacles.insert(self.posid,Obstacle('none',self.colisRect,self.posid)) 
            if doAnimation and self.animation is not None:      
                for i in range(len(self.animation)):
                    screen.fill('white')
                    if not inStruct:
                        for tile in tiles:
                            if tile.id==player.id:
                                tile.loadTile()
                    else:
                        for structure in structures:
                            if structure.id==player.id:
                                structure.loadTile()
                    screen.blit(self.animation[i],self.rect)
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
            exec(self.script,globals())
