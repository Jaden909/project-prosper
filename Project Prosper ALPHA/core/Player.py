class Player:
    def __init__(self,x,y,maxHp,maxHunger,sprites):
            self.x=x
            self.y=y
            self.currentBiome='unknown'
            self.playerRect=pygame.rect.Rect(self.x,self.y,30,32)
            self.maxHp=maxHp
            self.hp=self.maxHp
            self.iFrames=10
            self.maxHunger=maxHunger
            self.hunger=self.maxHunger
            self.hungerPoints=100
            self.healCooldown=100
            self.starveCooldown=100
            self.deathCooldown=300
            self.direction='down'
            self.sprites=sprites
            self.dead=False
            self.spawnPoint=128
            self.stunned=False
            self.stunDuration=0
    def listenInputs(self):
            global goRight, goLeft, goUp, goDown
            if not self.dead:
                blockMovement=False
                if keys[pygame.key.key_code(controls['right'])] or goRight:
                    self.direction='right'
                    goRight=False
                    futureRect=self.playerRect.copy()
                    futureRect.move_ip(2,0)
                    for obstacle in obstacles:
                        if obstacle.colisRect.colliderect(futureRect):
                            if obstacle.blockMovement:
                                #print(obstacle.colisRect.top,obstacle.colisRect.left)
                                #print(futureRect.top,futureRect.left)
                                blockMovement=True
                                break
                    if not blockMovement and not self.stunned:
                        self.x+=2
                        self.doHunger()

                    #screen.blit(self.sprites[self.direction],(self.x,self.y))
                if keys[pygame.key.key_code(controls['left'])] or goLeft:
                    self.direction='left'
                    goLeft=False
                    blockMovement=False
                    futureRect=self.playerRect.copy()
                    futureRect.move_ip(-2,0)
                    for obstacle in obstacles:
                        if obstacle.colisRect.colliderect(futureRect):
                            if obstacle.blockMovement:
                                #print(obstacle.colisRect.top,obstacle.colisRect.left)
                                #print(futureRect.top,futureRect.left)
                                blockMovement=True
                                break
                    else:
                        blockMovement=False
                    if not blockMovement and not self.stunned:
                        self.x-=2
                        self.doHunger()
                    #screen.blit(self.sprites[self.direction],(self.x,self.y))
                #screen.blit(playerImg,(self.x,self.y))
                if keys[pygame.key.key_code(controls['up'])] or goUp:
                    self.direction='up'
                    goUp=False
                    blockMovement=False
                    futureRect=self.playerRect.copy()
                    futureRect.move_ip(0,-2)
                    for obstacle in obstacles:
                        if obstacle.colisRect.colliderect(futureRect):
                            if obstacle.blockMovement:
                                #print(obstacle.colisRect.top,obstacle.colisRect.left)
                                #print(futureRect.top,futureRect.left)
                                blockMovement=True
                                break
                    if not blockMovement and not self.stunned:
                        self.y-=2
                        self.doHunger()
                    #screen.blit(self.sprites[self.direction],(self.x,self.y))
                if keys[pygame.key.key_code(controls['down'])] or goDown:
                    self.direction='down'
                    blockMovement=False
                    goDown=False
                    futureRect=self.playerRect.copy()
                    futureRect.move_ip(0,2)
                    for obstacle in obstacles:
                        if obstacle.colisRect.colliderect(futureRect):
                            if obstacle.blockMovement:
                                #print(obstacle.colisRect.top,obstacle.colisRect.left)
                                #print(futureRect.top,futureRect.left)
                                blockMovement=True
                                break
                    if not blockMovement and not self.stunned:
                        self.y+=2
                        self.doHunger()
                if carryingItem:
                    if heldItemm.type=='Tool':
                        self.itemSprite=pygame.transform.scale(pygame.image.load(PurePath('items\\'+heldItemm.spriteLocation)),(16,16))
                        self.itemSpriteFlipped=pygame.transform.flip(self.itemSprite,True,False)
                    else:
                        self.itemSprite=pygame.transform.scale(heldItemm.sprite,(16,16))
                        self.itemSpriteFlipped=pygame.transform.flip(self.itemSprite,True,False)
                    if self.direction=='right' and 'hideWhenHolding' not in heldItemm.tags:
                        screen.blit(self.itemSprite,(self.x+22,self.y+6))
                    elif self.direction=='left'and 'hideWhenHolding' not in heldItemm.tags:
                        screen.blit(self.itemSpriteFlipped,(self.x-8,self.y+6))
                    if not self.iFrames%2 and self.iFrames!=0:
                        pass
                    elif not self.stunned:
                        screen.blit(self.sprites[self.direction+'Hold'],(self.x,self.y))
                    elif self.stunned:
                        playerCopy=self.sprites[self.direction].copy()
                        playerCopy.blit(stun,(0,0))
                        screen.blit(playerCopy,(self.x,self.y))
                    if self.direction=='down'and 'hideWhenHolding' not in heldItemm.tags:
                        screen.blit(self.itemSprite,(self.x+8,self.y+6))
                else:
                    if not self.iFrames%2 and self.iFrames!=0:
                        pass
                    elif not self.stunned:
                        screen.blit(self.sprites[self.direction],(self.x,self.y))
                    elif self.stunned:
                        playerCopy=self.sprites[self.direction].copy()
                        playerCopy.blit(stun,(0,0))
                        screen.blit(playerCopy,(self.x,self.y))
                self.playerRect=pygame.rect.Rect(self.x,self.y,30,32)
                if self.iFrames>0:
                    self.iFrames-=1
                if self.stunned:
                    self.stunDuration-=1
                    if self.stunDuration<=0:
                        self.stunned=False
            else:
                #print(self.deathCooldown)
                self.deathCooldown-=1
                if self.deathCooldown<=0:
                    self.hp=self.maxHp/2
                    self.hunger=self.maxHunger
                    self.id=self.spawnPoint
                    self.dead=False
                    self.deathCooldown=300
            
    def getBiome(self):
        for tile in tiles:
            if tile.checkCollisions():
                self.id=tile.id
                #print(player1.id)
    def hurt(self,damage,iFrames=40):
        if self.iFrames==0:
            self.hp-=damage
            self.iFrames=iFrames
        if self.hp<=0:
            self.dead=True
    def doHunger(self):
        self.hungerPoints-=1
        if self.hungerPoints==0:
            self.hunger-=1
            self.hungerPoints=1000
        if self.hunger<=0 and self.starveCooldown<=0:
            self.hurt(1,20)
            self.starveCooldown=100
        self.heal()
        #print(self.hunger,self.hungerPoints)
        self.starveCooldown-=1
    def heal(self):
        if self.hp<self.maxHp and self.hunger>0 and self.healCooldown<=0:
            self.hunger-=1
            self.hp+=5
            self.healCooldown=100
        self.healCooldown-=1
    def stun(self,duration):
        self.stunned=True
        self.stunDuration=duration
        