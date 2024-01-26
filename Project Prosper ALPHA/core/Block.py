#DEPRECATED
class Block(Obstacle):
    def __init__(self,id):
        pass
        #self.id=id
        #self.data=blocks[self.id]
        #self.name=self.data['Name']
        #self.sprite=pygame.image.load(self.data['Sprite'])
        #self.parentItem=getItem(self.data['ParentId'])
        #if self.data['Script'] is not None:
        #    self.script=compile(open('scripts\\'+self.data['Script']+'.py').read(),self.data['Script']+'.py','exec')
        #else:
        #    self.script=None
    def interact(self):
        pass
        #for block in blockObjs:
        #    if block.name==self.type:
        #        if block.script is not None:
        #            exec(block.script)