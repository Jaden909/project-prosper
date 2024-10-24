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
        self.canBePlaced=None
        try:
            self.sprite=pygame.image.load(PurePath('items',self.spriteLocation))
        except Exception as e:
            self.sprite=pygame.image.load(PurePath('items','unknown.png'))
            self.name=f'Object failed to load ({self.itemId})'
            self.tooltip='It\'ll buff. Caused by missing image in Item data.'
            #print(traceback.format_exc())
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
                if 'canBePlaced' in self.tags:
                    self.canBePlaced=self.tags['canBePlaced']
                    #print('joun was set')
                else:
                    self.canBePlaced=None
                if 'lscript' in self.tags:
                    self.lscript=compile(open(PurePath(f"scripts",f"{self.tags['lscript']}")).read(),PurePath(f"scripts",f"{self.tags['lscript']}"),'exec')
                else:
                    self.lscript=None
                if 'rscript' in self.tags:
                    self.rscript=compile(open(PurePath(f"scripts",f"{self.tags['rscript']}")).read(),PurePath(f"scripts",f"{self.tags['rscript']}"),'exec')
                else:
                    self.rscript=None
            except Exception as e:
                print(f'Loading tags of {self.name} (Id:{self.itemId}) failed. Item will have no tags.')
                print(f'The error was: {e}')
                self.tags=[]
                self.holdScript=None
                self.canBePlaced=None
                self.lscript=None
                self.rscript=None
        except: 
            self.tags=[] 
            self.holdScript=None
            self.lscript=None
            self.rscript=None
        try:
            self.tooltip
        except:
            try:
                self.tooltip=self.data['Tooltip']
            except:
                self.tooltip=''
        if advancedTooltips:
            if self.tooltip=='':
                self.tooltip+=f'Id: {self.itemId}'
            else:
                self.tooltip+=f' Id: {self.itemId}'
        #print(self.tooltip)
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
