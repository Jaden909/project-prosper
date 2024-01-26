if currentEnemy.rect.centerx>player.playerRect.centerx and currentEnemy.delay<=0:
    blockMovement=False
    futureRect=currentEnemy.rect.copy()
    futureRect.move_ip(-1,0)
    for obstacle in obstacles:
        if obstacle.colisRect.colliderect(futureRect):
            if obstacle.blockMovement:
                #print(obstacle.colisRect.top,obstacle.colisRect.left)
                #print(futureRect.top,futureRect.left)
                blockMovement=True
                break
    if not blockMovement: 
        currentEnemy.rect.centerx-=1
    currentEnemy.delay+=currentEnemy.moveDelay
elif currentEnemy.rect.centerx<player.playerRect.centerx and currentEnemy.delay<=0:
    blockMovement=False
    futureRect=currentEnemy.rect.copy()
    futureRect.move_ip(1,0)
    for obstacle in obstacles:
        if obstacle.colisRect.colliderect(futureRect):
            if obstacle.blockMovement:
                #print(obstacle.colisRect.top,obstacle.colisRect.left)
                #print(futureRect.top,futureRect.left)
                blockMovement=True
                break
    if not blockMovement: 
        currentEnemy.rect.centerx+=1
    currentEnemy.delay+=currentEnemy.moveDelay
if currentEnemy.rect.centery>player.playerRect.centery and currentEnemy.delay<=0:
    blockMovement=False
    futureRect=currentEnemy.rect.copy()
    futureRect.move_ip(0,-1)
    for obstacle in obstacles:
        if obstacle.colisRect.colliderect(futureRect):
            if obstacle.blockMovement:
                #print(obstacle.colisRect.top,obstacle.colisRect.left)
                #print(futureRect.top,futureRect.left)
                blockMovement=True
                break
    if not blockMovement: 
        currentEnemy.rect.centery-=1
    currentEnemy.delay+=currentEnemy.moveDelay
elif currentEnemy.rect.centery<player.playerRect.centery and currentEnemy.delay<=0:
    blockMovement=False
    futureRect=currentEnemy.rect.copy()
    futureRect.move_ip(0,1)
    for obstacle in obstacles:
        if obstacle.colisRect.colliderect(futureRect):
            if obstacle.blockMovement:
                #print(obstacle.colisRect.top,obstacle.colisRect.left)
                #print(futureRect.top,futureRect.left)
                blockMovement=True
                break
    if not blockMovement: 
        currentEnemy.rect.centery+=1
    currentEnemy.delay+=currentEnemy.moveDelay
currentEnemy.delay-=1