class Tool(Item):
    def __init__(self,id) -> None:
        #Item Stuff
        self.itemId=id
        self.data=items[id]
        self.name=self.data['Name']
        self.maxStackSize=1
        self.spriteLocation=self.data['Sprite']
        self.sprite=pygame.image.load(PurePath('items\\'+self.spriteLocation))
        self.baseSprite=pygame.image.load(PurePath('items\\'+self.spriteLocation))
        
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

                    self.lscript=compile(open(PurePath(f'scripts\\{tag[7:]}')).read(),f'scripts\\{tag[7:]}','exec')
                #Called on right click
                elif tag[:7]=='rscript':
                    if tag[7:]=='None':
                        self.rscript=None
                        continue

                    self.rscript=compile(open(PurePath(f'scripts\\{tag[7:]}')).read(),f'scripts\\{tag[7:]}','exec')
                elif tag[:6]=='damage':
                    self.damage=int(tag[6:])
                elif tag[:10]=='SwingSpeed':
                    self.speed=int(tag[10:])
        
        except Exception as e:
            self.tags=[]
            self.harvestLevel=0
            self.durability=0
            self.lscript=None
            self.rscript=None
            self.damage=1
            print(f'Loading of tool {self.name} failed. Tool will be dysfunctional, but should still work as an item.')
            print(e)  
        try:
            self.tooltip=self.data['Tooltip']
        except:
            self.tooltip=''
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
            exec(self.lscript,globals())
    def rclick(self):
        if self.rscript!=None:
            global currentTool
            currentTool=self
            exec(self.rscript,globals())
    def reloadSprite(self):
        if self.durability!=self.maxDurability:

            self.sprite=self.baseSprite
            progressBar=pygame.surface.Surface((round(self.durability*32/self.maxDurability),4))
            progressBar.fill('green')
            self.sprite.blit(progressBar,(0,28))