ammo=find(59,range(24))
if ammo is not None or infinity:
    if not infinity:
        removeOne(ammo['Slot'])
    #Shoot bone
    currentProjectile='bone'
    for pool in projectilePools:
        if pool==currentProjectile:
            for projectile in  projectilePools[pool]:
                if not projectile.active:
                    projectile.spawn((player1.x+24,player1.y+24))
                    break