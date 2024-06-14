if not invOpen and not smeltOpen and not chestOpen:
    pygame.mouse.set_cursor(pygame.cursors.Cursor((14,14),pygame.image.load(PurePath('misc','crosshair.png'))))
    cursorChange=True
else:
    cursorChange=False 
mx,my=pygame.mouse.get_pos()
correctionAngle=225
dx, dy = mx - player1.playerRect.centerx, player1.playerRect.centery - my
angle = math.degrees(math.atan2(-dy, dx)) - correctionAngle
#screen.blit(,(player1.x,player1.y))
bowSurf=pygame.Surface((32,32))
bowSurf.blit(getItem(currentItem['Item']).sprite,(0,0))
bowSurf,bowSurfCopy=pygame.transform.rotate(bowSurf,-angle),pygame.transform.rotate(bowSurf,-angle)
bowSurf.set_colorkey((0,0,0))
screen.blit(bowSurf,(player1.x-bowSurfCopy.get_width()/2+16,player1.y-bowSurfCopy.get_height()/2+16))