print('give')
for slot in inventory:
    if slot['Item']==None and slot['Amount']==0:
        try:
            addStack(inventory.index(slot),int(commandParts[1]),int(commandParts[2]))
            break
        except Exception as e:
            send('Bad/no values given for give command')
            break
            #print(e)