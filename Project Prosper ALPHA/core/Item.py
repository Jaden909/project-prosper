class Item:
    def __init__(self,itemId:int,customPath=None):
        self.itemId=itemId
        if not customPath:
            self.data=items[self.itemId]
        else:
            self.data=PyEngine.load(PurePath('mods',customPath))[self.itemId]

        self.name=self.data['Name']
        self.maxStackSize=self.data['MaxStackSize']
        self.spriteLocation=self.data['Sprite']
        try:
            self.sprite=pygame.image.load(PurePath('items',self.spriteLocation))
        except:
            self.sprite=pygame.image.load(PurePath('items','unknown.png'))
            self.name=f'Object failed to load ({self.itemId})'
            self.tooltip='It\'ll buff. Caused by missing image in Item data.'
        self.type=self.data['Type']
        try:
            self.tags=self.data['Tags']
            try:

            
                if 'solidFuel' in self.tags:
                    if 'burnTime' in self.tags:
                        self.burnTime=int(self.tags['burnTime'])
                    else:
                        print(f'Warning: item {self.name} is missing the burnTime tag. Its fueling functions are disabled.')
                        self.tags.pop('solidFuel')
                if 'hideWhenHolding' in self.tags:
                    self.hideWhenHolding=True
                else:
                    self.hideWhenHolding=False
                if 'holdScript' in self.tags:
                    self.holdScript=compile(PurePath('scripts',self.tags['holdScript']),PurePath('scripts',self.tags['holdScript']),'exec')
                else:
                    self.holdScript=None
            except Exception as e:
                print(f'Loading tags of {self.name} (Id:{self.itemId}) failed. Item will have no tags.')
                print(f'The error was: {e}')
                self.tags=[]
                self.holdScript=None
        except: 
            self.tags=[] 
            self.holdScript=None
        try:
            self.tooltip
        except:
            try:
                self.tooltip=self.data['Tooltip']
            except:
                self.tooltip=''
    def pickUp(self):
        global invFull
        #inventory.reverse()
        for item in inventory[0:25]:
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
