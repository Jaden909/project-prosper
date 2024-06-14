class Mod:
    def __init__(self,name,author,version,icon,loopScript):
        self.name=name
        self.author=author
        self.version=version
        self.icon=icon
        self.loopScript=loopScript
        modObjs.append(self)
    def loop(self):
        if self.loopScript is not None:
            exec(self.loopScript)
    
    