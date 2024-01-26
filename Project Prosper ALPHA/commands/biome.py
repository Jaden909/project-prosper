for tile in level:
    try:
        if commandParts[1]==tile:
            player.id=level.index(tile)
            break
    except IndexError:
        send('Biome command requires string of biome to go to')
        break