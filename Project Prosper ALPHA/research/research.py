import pygame,PyEngine
from pathlib import PurePath
pygame.init()
research=[]
the1x1=pygame.image.load(PurePath('research','sprites','1x1.png'))
x1SpriteSheet=PyEngine.loadSpriteSheet(PurePath('research','sprites','x1.png'),32,3)
y1SpriteSheet=PyEngine.loadSpriteSheet(PurePath('research','sprites','y1.png'),32,3)
mainSpriteSheet=PyEngine.loadSpriteSheet(PurePath('research','sprites','main.png'),32,9)
y1Sprites={'start':y1SpriteSheet[0],'middle':y1SpriteSheet[1],'end':y1SpriteSheet[2]}
x1Sprites={'start':x1SpriteSheet[0],'middle':x1SpriteSheet[1],'end':x1SpriteSheet[2]}
mainSprites={'topLeft':mainSpriteSheet[0],'topMiddle':mainSpriteSheet[1],'topRight':mainSpriteSheet[2],'leftMiddle':mainSpriteSheet[3],'center':mainSpriteSheet[4],'rightMiddle':mainSpriteSheet[5],'bottomLeft':mainSpriteSheet[6],'bottomMiddle':mainSpriteSheet[7],'bottomRight':mainSpriteSheet[8]}
#Goals
#Auto-wrap X
#Multi-parent X
#Change line origins X
class ResearchWindow:
    def __init__(self,width,height,gridsize):
        self.width,self.height=width,height
        self.gridsize=gridsize
        self.window=pygame.Surface((self.width,self.height))
        self.font=None
        self.fontColor=None
        self.globalCost=None
        self.remainingCost=None
        self.backButt=PyEngine.GameButton(0,0,None,imageRes=32,image=PurePath('research','sprites','backButt.png'),active=False)
        self.multi=1
    def update(self):
        "Updates the research window. Must be placed in a loop to work properly"
        self.window.fill('grey')
        for res in research:
            #y1
            if res.gridh==1:
                if res.gridw==1:
                    self.window.blit(the1x1,(res.gridpos[0]*self.gridsize,res.gridpos[1]*self.gridsize))
                if res.gridw==2:
                    self.window.blit(y1Sprites['start'],(res.gridpos[0]*self.gridsize,res.gridpos[1]*self.gridsize))
                    self.window.blit(y1Sprites['end'],((res.gridpos[0]+1)*self.gridsize,res.gridpos[1]*self.gridsize))
                if res.gridw>2:
                    self.window.blit(y1Sprites['start'],(res.gridpos[0]*self.gridsize,res.gridpos[1]*self.gridsize))
                    for i in range(res.gridw-1):
                        self.window.blit(y1Sprites['middle'],((res.gridpos[0]+i)*self.gridsize,res.gridpos[1]*self.gridsize))
                    self.window.blit(y1Sprites['end'],((res.gridpos[0]+res.gridw-1)*self.gridsize,res.gridpos[1]*self.gridsize))
            #x1
            elif res.gridw==1:
                if res.gridh==1:
                    self.window.blit(the1x1,(res.gridpos[0]*self.gridsize,res.gridpos[1]*self.gridsize))
                if res.gridh==2:
                    self.window.blit(x1Sprites['start'],(res.gridpos[0]*self.gridsize,res.gridpos[1]*self.gridsize))
                    self.window.blit(x1Sprites['end'],((res.gridpos[0])*self.gridsize,(res.gridpos[1]+1)*self.gridsize))
                if res.gridh>2:
                    self.window.blit(x1Sprites['start'],(res.gridpos[0]*self.gridsize,res.gridpos[1]*self.gridsize))
                    for i in range(res.gridh-1):
                        self.window.blit(x1Sprites['middle'],((res.gridpos[0])*self.gridsize,(res.gridpos[1]+i)*self.gridsize))
                    self.window.blit(x1Sprites['end'],((res.gridpos[0])*self.gridsize,(res.gridpos[1]+res.gridh-1)*self.gridsize))
            #main
            else:
                #Top Row
                self.window.blit(mainSprites['topLeft'],(res.gridpos[0]*self.gridsize,(res.gridpos[1])*self.gridsize))
                for x in range(res.gridw-1):
                    self.window.blit(mainSprites['topMiddle'],((res.gridpos[0]+x+1)*self.gridsize,(res.gridpos[1])*self.gridsize))
                self.window.blit(mainSprites['topRight'],((res.gridpos[0]+res.gridw-1)*self.gridsize,(res.gridpos[1])*self.gridsize))
                #Middle Rows
                for y in range(res.gridh-2):
                    self.window.blit(mainSprites['leftMiddle'],(res.gridpos[0]*self.gridsize,(res.gridpos[1]+y+1)*self.gridsize))
                    for x in range(res.gridw-1):
                        self.window.blit(mainSprites['center'],((res.gridpos[0]+x+1)*self.gridsize,(res.gridpos[1]+y+1)*self.gridsize))
                    self.window.blit(mainSprites['rightMiddle'],((res.gridpos[0]+res.gridw-1)*self.gridsize,(res.gridpos[1]+y+1)*self.gridsize))
                #Bottom Rows
                self.window.blit(mainSprites['bottomLeft'],(res.gridpos[0]*self.gridsize,(res.gridpos[1]+res.gridh-1)*self.gridsize))
                for x in range(res.gridw-1):
                    self.window.blit(mainSprites['bottomMiddle'],((res.gridpos[0]+x+1)*self.gridsize,(res.gridpos[1]+res.gridh-1)*self.gridsize))
                self.window.blit(mainSprites['bottomRight'],((res.gridpos[0]+res.gridw-1)*self.gridsize,(res.gridpos[1]+res.gridh-1)*self.gridsize))    
            if res.parents is not None:
                res.locked=True
                for parent in res.parents:
                    if res.lineFrom=='bottom':
                        point0=(research[parent].rect.midbottom)
                    elif res.lineFrom=='right':
                        point0=(research[parent].rect.midright)
                    if res.lineTo=='top':
                        point1=res.rect.midtop
                    elif res.lineTo=='left':
                        point1=res.rect.midleft
                    pygame.draw.aaline(self.window,'black',point0,point1)
                for parent in res.parents:    
                    if not self.getOutputs()[parent]:
                        break
                else:
                    res.locked=False
            if res.title is not None:
                if self.font is None:
                    print('ResearchWindow requires a font to render text. Set one using the setFont method.')
                else:
                    self.window.blit(self.font.render(res.title,False,self.fontColor),(res.rect.centerx-self.font.size(res.title)[0]/2,res.rect.top+2))
            if res.desc is not None:
                if self.font is None:
                    print('ResearchWindow requires a font to render text. Set one using the setFont method.')
                else:
                    self.window.blit(self.font.render(res.desc,False,self.fontColor,wraplength=res.gridw*self.gridsize-10),(res.rect.left+5,res.rect.top+self.font.size('qwertyuiopasdfghjklzxcvbnm')[1]+5)) 
            if res.cost is not None and res.costIcon is not None:
                self.window.blit(res.costIcon,(res.rect.left+2,res.rect.bottom-20))
                self.window.blit(self.font.render(res.cost,False,self.fontColor if res.canAfford else 'red'),(res.rect.left+25,res.rect.bottom-20))
            if not res.locked:   
                res.button.listen(self.window)
                res.button.show(self.window)  
            else:
                self.blackout=pygame.Surface(res.rect.size)
                self.blackout.set_alpha(200)
                self.window.blit(self.blackout,res.rect)
            if res.researching and self.remainingCost is not None:
                if self.remainingCost>=0:
                    self.backProgressBar=pygame.Surface((res.rect.width-20,20))
                    self.progressBar=pygame.Surface(((res.rect.width-20)*(res.progress/res.completeTime),20))
                    self.backProgressBar.fill('grey')
                    self.progressBar.fill('green')
                    self.window.blit(self.backProgressBar,(res.rect.left+10,res.rect.bottom-60))
                    self.window.blit(self.progressBar,(res.rect.left+10,res.rect.bottom-60))
                    res.progress+=1
                    res.remainingTime-=1
                    #print(res.remainingTime)
                    #print(self.remainingCost)
                    if res.remainingTime==0:
                        res.output=True
                        res.researching=False
                elif res.researching:
                    res.progress=0
                    res.remainingTime=res.completeTime*self.multi
            elif res.researching and self.remainingCost is None:
                    self.backProgressBar=pygame.Surface((res.rect.width-20,20))
                    self.progressBar=pygame.Surface(((res.rect.width-20)*(res.progress/res.completeTime),20))
                    self.backProgressBar.fill('grey')
                    self.progressBar.fill('green')
                    self.window.blit(self.backProgressBar,(res.rect.left+10,res.rect.bottom-60))
                    self.window.blit(self.progressBar,(res.rect.left+10,res.rect.bottom-60))
                    res.progress+=1
                    res.remainingTime-=1
                    #print(res.remainingTime)
                    #print(self.remainingCost)
                    if res.remainingTime==0:
                        res.output=True
                        res.researching=False
            self.backButt.listen(self.window)
            self.backButt.show(self.window)
            self.window.blit(self.font.render('Research v0.0',False,'black'),(self.width-100,16))
            
    def blit(self,screen,pos):
        screen.blit(self.window,pos)
    def setFont(self,font:pygame.Font,color:pygame.Color):
        "Set font of all research text"
        self.font=font
        self.fontColor=color
    def updateCosts(self,vars):
        "Checks values of variables given to Research objects. Will throw an error if any of those variables aren't present in vars."
        for res in research:
            if res.trueCost is not None:
                res.updateCost(vars[res.costVar])
            if res.researching and self.globalCost:
                vars[self.globalCost]-=1
                self.remainingCost=vars[self.globalCost]
    def getOutputs(self):
        "Gets outputs of all researches, ordered by id number"
        output=[]
        for res in research:
            output.append(res.output)
        return output
    def bindBack(self,func):
        "Bind a function to the Research window's back button"
        self.backButt.function=func
    def setGlobalCost(self,var:str):
        "Set variable to decrement by one each frame research is being performed"
        self.globalCost=var
    def setCompleteTimeMultiplier(self,multiplier):
        self.multi=multiplier
class Research:
    def __init__(self,gridw,gridh,gridpos,title,desc,gridsize,parents=None,cost=None,costIcon=None,trueCost=None,costVar=None,completeTime=0,lineFrom='bottom',lineTo='top'):
        self.gridw,self.gridh=gridw,gridh
        self.gridpos=gridpos
        self.rect=pygame.rect.Rect(self.gridpos[0]*gridsize,self.gridpos[1]*gridsize,self.gridw*gridsize,gridh*gridsize)
        self.button=PyEngine.GameButton(self.rect.right-35,self.rect.bottom-35,self.research,image=PurePath('research','sprites','buyButt.png'),imageRes=32,active=False)
        self.title,self.desc=title,desc
        self.parents=parents
        self.cost=cost
        self.costIcon=pygame.image.load(PurePath('research','icons',costIcon))
        self.trueCost=trueCost
        self.costVar=costVar
        self.canAfford=False
        self.output=False
        self.locked=True if self.parents else False
        self.completeTime=completeTime
        self.remainingTime=completeTime
        self.progress=0
        self.researching=False
        self.lineFrom=lineFrom
        self.lineTo=lineTo
        self.id=len(research)
        research.append(self)
    def updateCost(self,var):
        if var>=self.trueCost:
            self.canAfford=True
        elif var<self.trueCost:
            self.canAfford=False
    def research(self):
        if self.canAfford and not self.output:
            if self.completeTime>0:
                self.researching=True
            #self.output=True
def loadTechTree(file):
    techTree=PyEngine.load(file)
    for tech in techTree:
        Research(**tech)
        #Research(tech['gridw'],tech['gridh'],tech['gridpos'],tech['title'],tech['desc'],tech['gridsize'],tech['parent'],tech['cost'],tech['costIcon'],tech['trueCost'],tech['costVar'],tech['completeTime'])
    