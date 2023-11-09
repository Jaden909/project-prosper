import pygame,PyEngine
pygame.init()
startTime = pygame.time.get_ticks()
startTime2 = pygame.time.get_ticks()
screen=pygame.display.set_mode((256,256))
clock=pygame.time.Clock()
delay=200
delay2=50
frame=0
frame2=0
done=False
done2=False
tree0=pygame.image.load('objects\\tree\\tree\\tree0.png')
tree1=pygame.image.load('objects\\tree\\tree\\tree1.png')
tree2=pygame.image.load('objects\\tree\\tree\\tree2.png')
tree3=pygame.image.load('objects\\tree\\tree\\tree3.png')
tree4=pygame.image.load('objects\\tree\\tree\\tree4.png')
ani=[tree0,tree1,tree2,tree3,tree4]
while True:
    for event in pygame.event.get():
        pass
    screen.fill('white')
    if not done:
        frame,startTime,done=PyEngine.animation(ani,200,screen,50,100,startTime,frame)
    if not done2:
        frame2,startTime2,done2=PyEngine.animation(ani,50,screen,150,100,startTime2,frame2)
    pygame.display.update()
    clock.tick(60)
    