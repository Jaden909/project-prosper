class Item:
    def __init__(self,itemId:int):
        self.itemId=itemId
        self.data=items[self.itemId]
        self.name=self.data['Name']
        self.maxStackSize=self.data['MaxStackSize']
        self.spriteLocation=self.data['Sprite']
        self.sprite=pygame.image.load('items\\'+self.spriteLocation)
        self.type=self.data['Type']
    def pickUp(self):
        global invFull
        inventory.reverse()
        for item in inventory[10:]:
            if item['Slot']>24:
                invFull=True
                break
            if item['Item']==self.itemId and item['Amount']<self.maxStackSize:
                item['Amount']+=1
                #print(item)
                
                break
            elif item['Item']is None:
                item['Item']=self.itemId
                item['Amount']+=1
                break
        inventory.reverse()