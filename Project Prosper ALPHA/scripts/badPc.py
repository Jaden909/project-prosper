
#236x212
#screen=pygame.display.set_mode((512,512))
#print('grgr')
researchWindow=research.ResearchWindow(512,512,32)
researchWindow.setFont(pygame.font.SysFont('fixed',12),'black')
researchWindow.bindBack(lambda:scriptQueue.clear())
#researchWindow.setGlobalCost('electricity')
pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
#ram=0
#electricity=10001
#research.Research(1,1,(2,7),'test','test',32) #0
#research.Research(4,1,(3,2),'test','test',32) #1
#research.Research(1,3,(4,5),'test','test',32) #2
#research.Research(3,1,(1,2),'test','test',32,0) #3
#
#research.Research(6,6,(9,3),'It\'s Joever','It is so incredibly Joever',32,None,'2 GB',pygame.image.load(PurePath('research','ram.png')),2048,'ram',10000) #4
#research.Research(3,1,(12,12),'test','test',32,4) #5
research.loadTechTree(PurePath('data','techTree.json'))



scriptQueue.append(lambda:researchWindow.updateCosts(globals()))
scriptQueue.append(lambda:researchWindow.update())
scriptQueue.append(lambda:researchWindow.blit(screen,(0,0)))


researches=researchWindow.getOutputs()


