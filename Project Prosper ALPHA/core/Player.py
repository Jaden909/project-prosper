class Player:
    def __init__(self,x,y):
            self.x=x
            self.y=y
            self.currentBiome='unknown'
            self.playerRect=pygame.rect.Rect(self.x,self.y,30,32)
    def listenInputs(self):
            keys=pygame.key.get_pressed()
            blockMovement=False
            if keys[pygame.K_d]:
                futureRect=self.playerRect.copy()
                futureRect.move_ip(2,0)
                for obstacle in obstacles:
                    if obstacle.colisRect.colliderect(futureRect):
                        if obstacle.type=='woodWall' or obstacle.type=='caveWall' or obstacle.type=='caveWall2' or obstacle.type=='caveWall3':
                            #print(obstacle.colisRect.top,obstacle.colisRect.left)
                            #print(futureRect.top,futureRect.left)
                            blockMovement=True
                            break
                if not blockMovement:
                    self.x+=2
                        
                screen.blit(playerImg,(self.x,self.y))
            if keys[pygame.K_a]:
                blockMovement=False
                futureRect=self.playerRect.copy()
                futureRect.move_ip(-2,0)
                for obstacle in obstacles:
                    if obstacle.colisRect.colliderect(futureRect):
                        if obstacle.type=='woodWall' or obstacle.type=='caveWall' or obstacle.type=='caveWall2' or obstacle.type=='caveWall3':
                            #print(obstacle.colisRect.top,obstacle.colisRect.left)
                            #print(futureRect.top,futureRect.left)
                            blockMovement=True
                            break
                else:
                    blockMovement=False
                if not blockMovement:
                    self.x-=2
                screen.blit(playerImg,(self.x,self.y))
            screen.blit(playerImg,(self.x,self.y))
            if keys[pygame.K_w]:
                blockMovement=False
                futureRect=self.playerRect.copy()
                futureRect.move_ip(0,-2)
                for obstacle in obstacles:
                    if obstacle.colisRect.colliderect(futureRect):
                        if obstacle.type=='woodWall' or obstacle.type=='caveWall' or obstacle.type=='caveWall2' or obstacle.type=='caveWall3':
                            #print(obstacle.colisRect.top,obstacle.colisRect.left)
                            #print(futureRect.top,futureRect.left)
                            blockMovement=True
                            break
                if not blockMovement:
                    self.y-=2
                screen.blit(playerImg,(self.x,self.y))
            if keys[pygame.K_s]:
                blockMovement=False
                futureRect=self.playerRect.copy()
                futureRect.move_ip(0,2)
                for obstacle in obstacles:
                    if obstacle.colisRect.colliderect(futureRect):
                        if obstacle.type=='woodWall' or obstacle.type=='caveWall' or obstacle.type=='caveWall2' or obstacle.type=='caveWall3':
                            #print(obstacle.colisRect.top,obstacle.colisRect.left)
                            #print(futureRect.top,futureRect.left)
                            blockMovement=True
                            break
                if not blockMovement:
                    self.y+=2
                screen.blit(playerImg,(self.x,self.y))
            self.playerRect=pygame.rect.Rect(self.x,self.y,30,32)
    def getBiome(self):
        for tile in tiles:
            if tile.checkCollisions():
                self.id=tile.id
                print(player.id)
