class Tool(Item):
    def __init__(self,id) -> None:
        #Item Stuff
        self.itemId=id
        self.data=items[id]
        self.name=self.data['Name']
        self.maxStackSize=1
        self.spriteLocation=self.data['Sprite']
        if sys.platform=='win32':
            self.sprite=pygame.image.load('items\\'+self.spriteLocation)
        elif sys.platform=='linux':
            self.sprite=pygame.image.load('items/'+self.spriteLocation)
        
        self.type=self.data['Type']
        try:
            self.tags=self.data['Tags']
            for tag in self.tags:
                if tag[:12]=='harvestLevel':
                    self.harvestLevel=int(tag[12:])
                elif tag[:10]=='durability':
                    self.durability=int(tag[10:])
                    self.maxDurability=self.durability
                elif tag[:8]=='burnTime':
                    self.burnTime=int(tag[8:])
                #Called on left click
                elif tag[:7]=='lscript':
                    if tag[7:]=='None':
                        self.lscript=None
                        continue
                    if sys.platform=='win32':
                        self.lscript=compile(open(f'scripts\\{tag[7:]}').read(),f'scripts\\{tag[7:]}','exec')
                    elif sys.platform=='linux':
                        self.lscript=compile(open(f'scripts/{tag[7:]}').read(),f'scripts\\{tag[7:]}','exec')
                #Called on right click
                elif tag[:7]=='rscript':
                    if tag[7:]=='None':
                        self.rscript=None
                        continue
                    if sys.platform=='win32':
                        self.rscript=compile(open(f'scripts\\{tag[7:]}').read(),f'scripts\\{tag[7:]}','exec')
                    elif sys.platform=='linux':
                        self.rscript=compile(open(f'scripts/{tag[7:]}').read(),f'scripts\\{tag[7:]}','exec')
        except Exception as e:
            self.tags=[]
            self.harvestLevel=0
            self.durability=0
            self.lscript=None
            self.rscript=None
            print(f'Loading of tool {self.name} failed. Tool will be dysfunctional, but should still work as an item.')
            print(e) 
        #if self.durability!=self.maxDurability:
        #    progressBar=pygame.surface.Surface((round(self.durability*32/self.maxDurability),4))
        #progressBar.fill('green')
        #self.sprite.blit(progressBar,(0,28))  
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
        
    #Tool Stuff
    def lclick(self):
        if self.lscript!=None:
            global currentTool
            currentTool=self
            exec(self.lscript)
    def rclick(self):
        if self.rscript!=None:
            global currentTool
            currentTool=self
            exec(self.rscript)
    def reloadSprite(self):
        if self.durability!=self.maxDurability:
            if sys.platform=='win32':
                self.sprite=pygame.image.load('items\\'+self.spriteLocation)
            elif sys.platform=='linux':
                self.sprite=pygame.image.load('items/'+self.spriteLocation)
            progressBar=pygame.surface.Surface((round(self.durability*32/self.maxDurability),4))
            progressBar.fill('green')
            self.sprite.blit(progressBar,(0,28))