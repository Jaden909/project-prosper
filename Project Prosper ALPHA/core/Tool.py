class Tool(Item):
    def __init__(self,id) -> None:
        #Item Stuff
        self.itemId=id
        self.data=items[id]
        self.name=self.data['Name']
        self.maxStackSize=1
        self.spriteLocation=self.data['Sprite']
        self.sprite=pygame.image.load(PurePath('items',self.spriteLocation))
        self.baseSprite=pygame.image.load(PurePath('items',self.spriteLocation))
        self.type=self.data['Type']
        try:

            self.tags=self.data['Tags']
            if 'harvestLevel' in self.tags:
                self.harvestLevel=int(self.tags['harvestLevel'])
            if 'durability' in self.tags:
                self.durability=int(self.tags['durability'])
                self.maxDurability=self.durability
            if 'burnTime' in self.tags:
                self.burnTime=int(self.tags['burnTime'])
            #Called on left click
            if 'lscript'in self.tags:
                if self.tags['lscript']is None:
                    self.lscript=None
                else:
                    self.lscript=compile(open(PurePath(f"scripts",f"{self.tags['lscript']}")).read(),PurePath(f"scripts",f"{self.tags['lscript']}"),'exec')
            #Called on right click
            if 'rscript'in self.tags:
                if self.tags['rscript']is None:
                    self.rscript=None
                else:
                    self.rscript=compile(open(PurePath(f"scripts",f"{self.tags['rscript']}")).read(),PurePath(f"scripts",f"{self.tags['rscript']}"),'exec')
            if 'damage'in self.tags:
                self.damage=int(self.tags['damage'])
            if 'SwingSpeed'in self.tags:
                self.speed=int(self.tags['SwingSpeed'])
            if 'solidFuel' in self.tags:
                if 'burnTime' in self.tags:
                    self.burnTime=int(tag[8:])
                else:
                    print(f'Warning: item {self.name} is missing the burnTime tag. Its fueling functions are disabled.')
                    self.tags.remove('solidFuel')
            if 'hideWhenHolding' in self.tags:
                self.hideWhenHolding=True
            else:
                self.hideWhenHolding=False
            if 'holdScript' in self.tags:
                self.holdScript=compile(open(PurePath("scripts",f"{self.tags['holdScript']}")).read(),PurePath(f"scripts",f"{self.tags['holdScript']}"),'exec')
            else:
                self.holdScript=None
        except Exception as e:
            self.tags=[]
            self.harvestLevel=0
            self.durability=0
            self.lscript=None
            self.rscript=None
            self.damage=1
            self.hideWhenHolding=False
            self.holdScript=None
            print(f'Loading of tool {self.name} failed. Tool will be dysfunctional, but should still work as an item.')
            print(e)  
        try:
            self.tooltip=self.data['Tooltip']
        except:
            self.tooltip=''
        if advancedTooltips:
            if self.tooltip=='':
                self.tooltip+=f'Id: {self.itemId}'
            else:
                self.tooltip+=f' Id: {self.itemId}'  
    #Tool Stuff
    def lclick(self):
        try:

            if self.lscript!=None:
                global currentTool
                currentTool=self
                exec(self.lscript,globals())
        except Exception as e:
            print(e)
    def rclick(self):
        try:
            if self.rscript!=None:
                global currentTool
                currentTool=self
                exec(self.rscript,globals())
        except Exception as e:
            print(e)
    def reloadSprite(self):
        if self.durability!=self.maxDurability:

            self.sprite=self.baseSprite
            progressBar=pygame.surface.Surface((round(self.durability*32/self.maxDurability),4))
            progressBar.fill('green')
            self.sprite.blit(progressBar,(0,28))