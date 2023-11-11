class Obstacle:
    def __init__(self,type,rect,id,dropsItem,isEntrance=False) -> None:
        self.type=type
        self.id=id
        if self.type=='tree':
            if rect.left>=20:
                self.colisRect=pygame.rect.Rect(rect.left+20,rect.top,rect.width,rect.height)
            else:
                self.colisRect=pygame.rect.Rect(0,rect.top,rect.width,rect.height)
            self.rect=rect
        else:
            self.rect=rect
            self.colisRect=rect
        if self.type=='mine':
            self.script=compile(open('scripts\\mine.py').read(),'mine.py','exec')
        elif self.type=='escape':
            self.script=compile(open('scripts\\escape.py').read(),'escape.py','exec')
        else:
            self.script=None
        
        self.dropsItem=dropsItem
        self.isEntrance=isEntrance

    def checkCollisionDamage(self,rect,animation,doAnimation,getLocation,destorySelf):
        if self.colisRect.colliderect(rect):
            
                #PyEngine.animation(tree,8,5,screen,self.rect.left,self.rect.top)
            if destorySelf and not inStruct:
                for tile in tiles:
                    if tile.id==player.id:
                        #print(self.id)
                        tile.obstacles.pop(self.id)
                        tile.obstacles.insert(self.id,Obstacle('none',self.colisRect,self.id,None)) 
            elif destorySelf:
                for structure in structures:
                    if structure.id==player.id:
                        #print(self.id)
                        structure.obstacles.pop(self.id)
                        structure.obstacles.insert(self.id,Obstacle('none',self.colisRect,self.id,None)) 
            if doAnimation:      
                for i in range(len(animation)):
                    screen.fill('white')
                    if not inStruct:
                        for tile in tiles:
                            if tile.id==player.id:
                                tile.loadTile()
                    else:
                        for structure in structures:
                            if structure.id==player.id:
                                structure.loadTile()
                    screen.blit(animation[i],self.rect)
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
                return {'Type':self.dropsItem,'Position':self.rect}
            return True,self.type
        return False
    def interact(self):
        global entrancePos
        if self.isEntrance:
            entrancePos=(self.rect)
        if self.script is not None:
            print('script')
            print(globals()['entrancePos'])
            exec(self.script,globals())