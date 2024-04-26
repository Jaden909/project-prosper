#_______________________________________Run Basic Ai First____________________________________________________________________________________________
exec(compile(open(PurePath('ai','basic.py')).read(),PurePath('ai','basic.py'),'exec'),globals())
exec(compile(open(PurePath('ai','basic.py')).read(),PurePath('ai','basic.py'),'exec'),globals())

#Boss ai here
# Vine attack: spawns a vine on the player. If they don't move by the time it fully grows, deal 10 damage and immobilize the player for 2 seconds (120 frames).
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
    branch=PyEngine.Projectile(32,32,2,0,200,False,boss1Stuff[3:])
#AI
queuedAttack=[]
if currentEnemy.hp<=500:
    maxAttackCooldown=30
else:
    maxAttackCooldown=80
if 'attackCooldown' not in globals():
    attackCooldown=maxAttackCooldown
if abs(currentEnemy.x-player.x)>=50 and attackCooldown<=0 and activeAttack is None or abs(currentEnemy.y-player.y)>=50 and attackCooldown<=0 and activeAttack is None:
    queuedAttack=random.choice(['branch'])
    attackCooldown=maxAttackCooldown
else:
    queuedAttack='melee'
if queuedAttack=='vine':
    activeAttack='vine'
    vineRect=pygame.Rect(player.x,player.y,32,32)
    boss1StartTime=pygame.time.get_ticks()
    boss1Frame=0
    queuedAttack=None
if queuedAttack=='branch':
    activeAttack='branch'
    branch=PyEngine.Projectile(32,32,2,0,200,False,boss1Stuff[3:],offset=(96,96))
    print((currentEnemy.rect.x+32,currentEnemy.rect.y+32))
    branch.spawn((currentEnemy.rect.x,currentEnemy.rect.y),target=(player.x,player.y))
    #branchRect=pygame.Rect(currentEnemy.x,currentEnemy.y,32,32)
    boss1StartTime=pygame.time.get_ticks()
    boss1Frame=0
    queuedAttack=None

if activeAttack=='vine':
    #print('vine')
    #screen.blit(boss1Stuff[0],(player.x,player.y))

    boss1Frame,boss1StartTime,boss1Done=PyEngine.animation(boss1Stuff[:3],600,screen,vineRect.x,vineRect.y,boss1StartTime,boss1Frame)
    if boss1Done:
        if vineRect.colliderect(player.playerRect):
            player.stun(100)
            player.hurt(10)
        activeAttack=None
if activeAttack=='branch':
    #boss1Frame,boss1StartTime,boss1Done=PyEngine.animation(boss1Stuff[3:],600,screen,branchRect.x,branchRect.y,boss1StartTime,boss1Frame)
    branch.update(screen)
    if branch.rect.colliderect(player.playerRect):
        player.hurt(30)
    #print(branch.lifetime)
    if branch.lifetime<=1:
        activeAttack=None
attackCooldown-=1


#_______________________________________________________Display Stuff_________________________________________________________________________________
screen.blit(currentEnemy.sprite,currentEnemy.rect)
screen.blit(bossBar,(-63,393))
#bossHealth.fill((255*(currentEnemy.hp/currentEnemy.maxHp),255*(currentEnemy.hp/currentEnemy.maxHp),255*(currentEnemy.hp/currentEnemy.maxHp)))
bossHealth=pygame.Surface((currentEnemy.hp/2,56))
bossHealth.fill('green')
screen.blit(bossHealth,(5,405))
if 'bossName' not in globals():
    bossName=PyEngine.TextBox('Forest Guardian',180,360,35,1,bossFont,30,True,True,'white','grey','black',2,(5,5))
else:
    bossName.update('Forest Guardian')
bossName.render(screen)

#screen.blit(bossFont.render(,True,'white'),(200,380))