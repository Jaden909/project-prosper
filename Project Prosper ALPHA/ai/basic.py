global delayNow,addDelay,currentEnemy,player1
delayNow=currentEnemy.delay
addDelay=False
if currentEnemy.rect.centerx>player1.playerRect.centerx and delayNow<=0:
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
elif currentEnemy.rect.centerx<player1.playerRect.centerx and delayNow<=0:
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
if currentEnemy.rect.centery>player1.playerRect.centery and delayNow<=0:
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
elif currentEnemy.rect.centery<player1.playerRect.centery and delayNow<=0:
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
if currentEnemy.rect.colliderect(player1.playerRect):
    player1.hurt(10)
if addDelay:
    currentEnemy.delay+=currentEnemy.moveDelay
currentEnemy.delay-=1
