#_______________________________________Run Basic Ai First____________________________________________________________________________________________
exec(compile(open(PurePath('ai','basic.py')).read(),PurePath('ai','basic.py'),'exec'),globals())
exec(compile(open(PurePath('ai','basic.py')).read(),PurePath('ai','basic.py'),'exec'),globals())

# Vine attack: spawns a vine on the player. If they don't move by the time it fully grows, deal 10 damage and immobilize the player for 2 seconds (240 frames).
# Branch throw: throws a branch at the player dealing 20 damage if it connects

# Load extra sprites for attacks
if 'boss1Stuff' not in globals():
    boss1Stuff=[]
    for sprite in currentEnemy.extraData:
        boss1Stuff.append(pygame.image.load(PurePath(*sprite)))
if 'activeAttack' not in globals():
    activeAttack=None
if 'boss1Frame' not in globals():
    boss1Frame=0
if 'branch' not in globals():
    branch=PyEngine.Projectile(32,32,1,-.001,200,False,boss1Stuff[3:],20,immune=[currentEnemy.rect])
#AI
queuedAttack=[]
if currentEnemy.hp<=500:
    maxAttackCooldown=30
else:
    maxAttackCooldown=80
if 'attackCooldown' not in globals():
    attackCooldown=maxAttackCooldown
if abs(currentEnemy.x-player1.x)>=50 and attackCooldown<=0 and activeAttack is None or abs(currentEnemy.y-player1.y)>=50 and attackCooldown<=0 and activeAttack is None:
    queuedAttack=random.choice(['branch','vine'])
    attackCooldown=maxAttackCooldown
else:
    queuedAttack='melee'
#Start vine attack
if queuedAttack=='vine':
    activeAttack='vine'
    vineRect=pygame.Rect(player1.x,player1.y,32,32)
    boss1StartTime=pygame.time.get_ticks()
    boss1Frame=0
    queuedAttack=None
#Start branch attack
if queuedAttack=='branch':
    activeAttack='branch'
    branch=PyEngine.Projectile(32,32,1,-.001,200,False,boss1Stuff[3:],offset=(96,96),damage=20,immune=[currentEnemy.rect])
    print((currentEnemy.rect.x+32,currentEnemy.rect.y+32))
    branch.spawn((currentEnemy.rect.x,currentEnemy.rect.y),target=(player1.x,player1.y))
    boss1StartTime=pygame.time.get_ticks()
    boss1Frame=0
    queuedAttack=None

#Vine Attack
if activeAttack=='vine':
    boss1Frame,boss1StartTime,boss1Done=PyEngine.animation(boss1Stuff[:3],600,screen,vineRect.x,vineRect.y,boss1StartTime,boss1Frame)
    if boss1Done:
        if vineRect.colliderect(player1.playerRect):
            player1.stun(240)
            player1.hurt(10)
        activeAttack=None
#Branch Attack
if activeAttack=='branch':
    branch.update(screen)
    if branch.rect.colliderect(player1.playerRect):
        player1.hurt(30)
    if branch.lifetime<=1:
        activeAttack=None
attackCooldown-=1


#_______________________________________________________Display Stuff_________________________________________________________________________________
screen.blit(currentEnemy.sprite,currentEnemy.rect)
screen.blit(bossBar,(-63,393))
bossHealth=pygame.Surface((currentEnemy.hp/2,56))
bossHealth.fill('green')
screen.blit(bossHealth,(5,405))
if 'bossName' not in globals():
    bossName=PyEngine.TextBox('Forest Guardian',180,360,35,1,bossFont,30,True,True,'white','grey','black',2,(5,5))
else:
    bossName.update('Forest Guardian')
bossName.render(screen)