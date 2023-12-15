if currentItem['Item']==17:
    cOb.sprite=pygame.image.load('objects\\xmasTree.png')
    currentItem['Amount']-=1
    if currentItem['Amount']==0:
        currentItem['Item']=None