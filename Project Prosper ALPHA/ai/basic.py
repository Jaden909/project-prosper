global delayNow,addDelay,currentEnemy,player
delayNow=currentEnemy.delay
addDelay=False
if currentEnemy.rect.centerx>player.playerRect.centerx and delayNow<=0:
    blockMovement=False
    futureRect=currentEnemy.rect.copy()
    futureRect.move_ip(-1,0)
    for obstacle in obstacles:
        if obstacle.colisRect.colliderect(futureRect):
            if obstacle.blockMovement:
                blockMovement=True
                break
    if not blockMovement: 
        currentEnemy.rect.centerx-=1
    addDelay=True
elif currentEnemy.rect.centerx<player.playerRect.centerx and delayNow<=0:
    blockMovement=False
    futureRect=currentEnemy.rect.copy()
    futureRect.move_ip(1,0)
    for obstacle in obstacles:
        if obstacle.colisRect.colliderect(futureRect):
            if obstacle.blockMovement:
                blockMovement=True
                break
    if not blockMovement: 
        currentEnemy.rect.centerx+=1
    addDelay=True
if currentEnemy.rect.centery>player.playerRect.centery and delayNow<=0:
    blockMovement=False
    futureRect=currentEnemy.rect.copy()
    futureRect.move_ip(0,-1)
    for obstacle in obstacles:
        if obstacle.colisRect.colliderect(futureRect):
            if obstacle.blockMovement:
                blockMovement=True
                break
    if not blockMovement: 
        currentEnemy.rect.centery-=1
    addDelay=True
elif currentEnemy.rect.centery<player.playerRect.centery and delayNow<=0:
    blockMovement=False
    futureRect=currentEnemy.rect.copy()
    futureRect.move_ip(0,1)
    for obstacle in obstacles:
        if obstacle.colisRect.colliderect(futureRect):
            if obstacle.blockMovement:
                blockMovement=True
                break
    if not blockMovement: 
        currentEnemy.rect.centery+=1
    addDelay=True
if currentEnemy.rect.colliderect(player.playerRect):
    player.hurt(10)
if addDelay:
    currentEnemy.delay+=currentEnemy.moveDelay
currentEnemy.delay-=1
