#print('l')
slashSpeed=getItem(currentItem['Item']).speed
if player1.direction=='left' and slashLDone:
    slashLFrame=0
    slashLStartTime=0
    slashLDone=False
elif player1.direction=='right'and slashDone:
    slashFrame=0
    slashStartTime=0
    slashDone=False
elif slashDone and slashLDone:
    slashFrame=0
    slashStartTime=0
    slashDone=False