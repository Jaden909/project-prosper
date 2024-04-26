print('give')
for slot in inventory:
    if slot['Item']==None and slot['Amount']==0:
        try:
            addStack(inventory.index(slot),int(commandParts[1]),int(commandParts[2]))
            send(f'Gave {int(commandParts[2])} {getItem(int(commandParts[1])).name} to Player')
            break
        except Exception as e:
            send('Bad/no values given for give command')
            print(e)
            break
            