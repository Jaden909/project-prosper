ammo=find(40,range(24))
if ammo is not None:
    removeOne(ammo['Slot'])
    #Shoot arrow
    currentProjectile='arrow'
    for pool in projectilePools:
        if pool==currentProjectile:
            for projectile in  projectilePools[pool]:
                if not projectile.active:
                    projectile.spawn((player1.x+24,player1.y+24))
                    break