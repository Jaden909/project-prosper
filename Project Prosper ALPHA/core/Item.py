class Item:
    def __init__(self,itemId:int):
        self.itemId=itemId
        self.data=items[self.itemId]
        self.name=self.data['Name']
        self.maxStackSize=self.data['MaxStackSize']
        self.spriteLocation=self.data['Sprite']
        if sys.platform=='windows':
            self.sprite=pygame.image.load('items\\'+self.spriteLocation)
        elif sys.platform=='linux':
            self.sprite=pygame.image.load('items/'+self.spriteLocation)
        self.type=self.data['Type']
        try:
            self.tags=self.data['Tags']
            if 'solidFuel' in self.tags:
                for tag in self.tags:
                    if tag[:8]=='burnTime':
                        self.burnTime=int(tag[8:])
                        break
                else:
                    print(f'Warning: item {self.name} is missing the burnTime tag. Its fueling functions are disabled.')
                    self.tags.remove('solidFuel')
        except:
            self.tags=[]
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