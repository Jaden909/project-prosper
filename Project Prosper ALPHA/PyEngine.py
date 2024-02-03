"""Game Engine for Python. Requires Pygame.""" 
import pygame,json,os,sys,importlib
pygame.init()
_mouseDown=False
buttons=[]
messages=[]
elements=[]

class Message:
    "Creates a message that can be sent and recieved"
    def __init__(self,name):
        self.name=name
        message={'name':self.name,'state':False}
        messages.append(message)
    def send(self):
        for message in messages:
            if message.get('name')==self.name:
                message.update(state=True)
    def unsend(self):
        for message in messages:
            if message.get('name')==self.name:
                message.update(state=False)
    def listen(self):
        for message in messages:
            if message.get('state'):
                return True
            else:
                return False
class GameButton:
    """Create a button that can trigger a function if clicked on or a message is recieved (if one is provided)"""
    def __init__(self,x:int=0,y:int=0,function=None,notHoverSprite:pygame.Surface='default',hover:bool=True,active:bool=True,hoverSprite:pygame.Surface='default',imageRes:int=64,image:str='Defaults\\DEFAULTBUTTON.png',imageResX:int=0,imageResY:int=0,message:Message=None,hoverAlt=None,hold=False):
        self.hovering=False
        #REQUIRED ARGS  
        self.x=x
        self.y=y    
        self.imageResX=imageResX
        self.imageResY=imageResY
        if imageResX !=0 or imageResY !=0:
            self.square=False
        else:
            self.square=True
        if image is not None:
            self.image=pygame.image.load(image).convert()
        self.imageRes=imageRes
        self.function=function
        self.hover=hover
        self.hoverSprite=hoverSprite
        self.notHoverSprite=notHoverSprite
        if hoverSprite=='default':
            self.hoverCursor=pygame.SYSTEM_CURSOR_HAND
        elif hoverSprite=='ibeam':
            self.hoverCursor=pygame.SYSTEM_CURSOR_IBEAM
        else:
            self.hoverCursor=pygame.cursors.Cursor((0,0),self.hoverSprite)
        if notHoverSprite=='default':
            self.notHoverCursor=pygame.SYSTEM_CURSOR_ARROW   
        elif notHoverSprite=='ibeam':
            self.notHoverCursor=pygame.SYSTEM_CURSOR_IBEAM 
        else:
            self.notHoverCursor=pygame.cursors.Cursor((0,0),self.notHoverSprite) 
        self.active=active
        self.message=message
        if hoverAlt is not None:
            self.hoverAlt=pygame.image.load(hoverAlt)
        else:
            self.hoverAlt=None
        self.hold=hold
        buttons.append(self)    
    #Blits button to screen provided
    def show(self,screen:pygame.surface.Surface):
        'Blit button to screen. Screen to blit to required. Requires defined image'
        screen.blit(self.image,(self.x,self.y))
    
    #Listens for mouse clicks: should be in a loop to work properly
    def listen(self,screen=None):    
        "Listens for clicks on the button. Should be in a loop."
        global _mouseDown
        if self.active:
            left,middle,right=pygame.mouse.get_pressed()
            #Hover
            if self.hover:    
                if self.square:
                    mouseX,mouseY=pygame.mouse.get_pos()
                    if mouseX>self.x and mouseX<self.x+self.imageRes and mouseY>self.y and mouseY<self.y+self.imageRes:
                        pygame.mouse.set_cursor(self.hoverCursor)
                        if self.hoverAlt is not None and screen is not None:
                            screen.blit(self.hoverAlt,(self.x,self.y))
                        self.hovering=True
                    elif self.hovering:
                        pygame.mouse.set_cursor(self.notHoverCursor)
                        self.hovering=False
                else:
                    mouseX,mouseY=pygame.mouse.get_pos()
                    if mouseX>self.x and mouseX<self.x+self.imageResX and mouseY>self.y and mouseY<self.y+self.imageResY:
                        pygame.mouse.set_cursor(self.hoverCursor)
                        if self.hoverAlt is not None and screen is not None:
                            screen.blit(self.hoverAlt,(self.x,self.y))
                        self.hovering=True
                    elif self.hovering:
                        pygame.mouse.set_cursor(self.notHoverCursor)
                        self.hovering=False
            
            #CLick Event
            if left and self.function:
                if self.square:    
                    mouseX,mouseY=pygame.mouse.get_pos()
                    if mouseX>self.x and mouseX<self.x+self.imageRes and mouseY>self.y and mouseY<self.y+self.imageRes and not _mouseDown:
                        self.function()
                        _mouseDown=True
                    elif mouseX>self.x and mouseX<self.x+self.imageRes and mouseY>self.y and mouseY<self.y+self.imageRes and self.hold and _mouseDown:
                        self.function()
                else:
                    mouseX,mouseY=pygame.mouse.get_pos()
                    if mouseX>self.x and mouseX<self.x+self.imageResX and mouseY>self.y and mouseY<self.y+self.imageResY and _mouseDown==False:
                        self.function()
                        _mouseDown=True
                    elif mouseX>self.x and mouseX<self.x+self.imageRes and mouseY>self.y and mouseY<self.y+self.imageRes and self.hold and _mouseDown:
                        self.function()
            else: _mouseDown=False
            if self.message and self.function:
                if self.message.listen():
                    self.function()
    def listenPulse(self):
        "Listens for hover once. Should NOT be used in a loop. Useful for controllers."
        if self.active and self.function:
            if self.square:    
                mouseX,mouseY=pygame.mouse.get_pos()
                if mouseX>self.x and mouseX<self.x+self.imageRes and mouseY>self.y and mouseY<self.y+self.imageRes:
                    self.function()
            else:
                mouseX,mouseY=pygame.mouse.get_pos()
                if mouseX>self.x and mouseX<self.x+self.imageResX and mouseY>self.y and mouseY<self.y+self.imageResY:
                    self.function() 
    def enable(self):
        self.active=True
    def disable(self):
        self.active=False
class Vector2:
    def __init__(self,x:int|float,y:int|float):
        self.value=(x,y)
    def translate(self,x=0,y=0):
        self.x=self.value.__getitem__(0)
        self.y=self.value.__getitem__(1)
        self.x+=x
        self.y+=y
        self.value=(self.x,self.y)
class staticImage:
    "Static Graphic that doesn't move. Requires x,y and image"
    def __init__(self,x:int,y:int,image:str):
        self.x=x
        self.y=y     
        self.image=pygame.image.load(image).convert()
    def show(self,screen):
        screen.blit(self.image,(self.x,self.y))
class TextBox:
    def __init__(self,text:str,x:int,y:int,height:int,width:int,fontName:str,size:int,bold:bool,italic:bool,textColor:str|tuple,bgColor:str|tuple|None,borderColor:str|tuple|None,borderWidth:int,textOffset:tuple):
        self.text=text
        self.x=x
        self.y=y
        self.height=height
        self.width=width
        self.textColor=textColor
        self.rect=pygame.rect.Rect(self.x,self.y,self.width,self.height)
        self.mask=pygame.Mask((self.width,self.height),True)
        self.bgColor=bgColor
        self.borderColor=borderColor
        self.borderWidth=borderWidth
        self.textOffset=textOffset
        self.font=pygame.font.Font(fontName,size)
        #self.font=pygame.font.SysFont(fontName,size,bold,italic)
        self.textBox=self.font.render(self.text,False,textColor)
        if bgColor is not None:
            self.bg=pygame.Surface((self.width,self.height))
            self.bg.fill(self.bgColor)
        else:
            self.bg=None
        elements.append(self)
    def update(self,text:str):
        'Update the text Displayed by the text box'
        self.text=text
        self.textBox=self.font.render(self.text,True,self.textColor)
    def render(self,screen:pygame.Surface,autoFit=True):
        if autoFit:
            self.rect.width=self.font.size(self.text)[0]+self.textOffset[0]*2
            self.width=self.font.size(self.text)[0]+self.textOffset[0]*2
            if self.bg is not None:
                self.bg=pygame.Surface((self.width,self.height))
                self.bg.fill(self.bgColor)
                screen.blit(self.bg,self.rect)
        screen.blit(self.textBox,self.rect.move(self.textOffset))
        if self.borderColor is not None:
            pygame.draw.rect(screen,self.borderColor,self.rect,self.borderWidth)
    def snapToMouse(self,borderX:int):
        if self.rect.right<borderX:
            self.rect.bottomleft=pygame.mouse.get_pos()
        if self.rect.right>borderX:
            self.rect.bottomright=pygame.mouse.get_pos()

        


def animation(moveList:list,frameDelay:int,screen:pygame.Surface,x,y,startTime:int,frame:int):
    """Pygame animation. returns current frame, startTime and done. Put this in a loop and supply the returned frame and startTime to work properly."""
    framee=frame
    currentTime = pygame.time.get_ticks()
    done=False
    if currentTime - startTime >= frameDelay:
        framee+=1
        startTime = currentTime
    if framee==len(moveList):
        framee=0
        done=True
        return framee,startTime,done
    try:
        screen.blit(moveList[frame],(x,y))
    except:
        pass
    return framee,startTime,done

def wasdInput(WFunction=None,AFunction=None,SFunction=None,DFunction=None):
    """Simple WASD/arrow keys input listener. Also supports arrow keys. Args are functions to run when respective key is pressed"""
    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT]or keys[pygame.K_a]and AFunction is not None:
        AFunction()
    if keys[pygame.K_RIGHT]or keys[pygame.K_d]and DFunction is not None:
        DFunction()
    if keys[pygame.K_DOWN]or keys[pygame.K_s]and SFunction is not None:
        SFunction()
    if keys[pygame.K_UP]or keys[pygame.K_w]and WFunction is not None:
        WFunction()
def enableAll():
    "Enables all created buttons"
    for button in buttons:
        button.enable()
def disableAll():
    "Disables all created buttons"
    for button in buttons:
        button.disable()
def listenAll(screen):
    "Listen on all active buttons at once"
    global buttons
    for button in buttons:
        if button.active:
            button.listen(screen)
def showAll(screen):
    "Show all active buttons at once"
    for button in buttons:
        if button.active:
            button.show(screen)
def listenPulseAll():
    "Listen pulse on all created buttons at once"
    global buttons
    for button in buttons:
        button.listenPulse()
def save(saveFile:str,save):
    "Save a dictionary of variables to a json file"
    _save=save
    with open(saveFile,'w') as f:
        json.dump(_save,f)
def load(saveFile:str)-> dict|list:
    "Load a dictionary of variables from a json file and return it"
    _save=json.load(open(saveFile))
    return _save
def checkHover(x1:int,x2:int,y1:int,y2:int,function):
    "Runs a function if mouse is in given area"
    mouseX,mouseY=pygame.mouse.get_pos()
    if mouseX>x1 and mouseX<x2 and mouseY>y1 and mouseY<y2:
        function()
def loadMods(modDir:str,loadingScreen:pygame.Surface=None,screen:pygame.Surface=None)->list:
    "Load mods in given directory. Returns list of loaded mods as Module objects. The folder containing each mod's files must start with an uppercase letter and the .py file must be the same name but lowercase."
    loadedMods=[]
    logList=[]
    log={}
    class Mod:
        def __init__(self,name,title,description,version,id,author,modified,script,icon):
            self.name=name
            self.title=title
            self.description=description
            self.version=version
            self.id=id
            self.author=author
            self.modified=modified
            self.script=script
            self.icon=icon
        def loop(self):
            self.script.loop()
        def init(self):
            self.script.init()
        def config(self):
            self.script.config() 
    for root, dirs, files in os.walk(f'{modDir}'):
            for name in dirs:
                if name[0].isupper():
                    
                    print('________________________________________________________________________________________')
                    logList.append('________________________________________________________________________________________')
                    print(f'Mod named {name} found.')
                    logList.append(f'Mod named {name} found.')
                    sys.path.insert(1,f'{modDir}\\{name}')
                    print(f'Folder named {name} successfully added to sys.path.')
                    logList.append(f'Folder named {name} successfully added to sys.path.')
                    meta=load(f'{modDir}\\{name}\\meta.json')
                    print(f'meta data of {name} successfully loaded.')
                    logList.append(f'meta data of {name} successfully loaded.')
                    mod=Mod(name,meta.get('title'),meta.get('description'),meta.get('version'),meta.get('id'),meta.get('author'),meta.get('modified'),importlib.import_module(name.lower()),None)
                    print(f'Mod object successfully created using the meta data of {name}.')
                    logList.append(f'Mod object successfully created using the meta data of {name}.')
                    loadedMods.append(mod)
                    print(f'{name}\'s mod object succesfully added to list of mods.')
                    print(f'Mod named {name} successfully loaded.')
                    logList.append(f'{name}\'s mod object succesfully added to list of mods.')
                    logList.append(f'Mod named {name} successfully loaded.')
                    if loadingScreen is not None:
                        screen.blit(loadingScreen,(0,0))    
    log.update(log=logList)
    save('log.json',log)
    print('Log saved to log.json file.')
    return loadedMods
def renderUI():
    for element in elements:
        element.render()
def autoWrap(text:str,width:int,font:pygame.font.Font,textColor, stopAtWhiteSpace=False):
    "returns a list of surfaces of text autowrapped to a given width"
    line=''
    lines=[]
    words=text.split(' ')
    if stopAtWhiteSpace:
        words=text.split('\n')
        for line in words:
            #print(line)
            lines.append(font.render(line,True,textColor))
        return lines
    for i in range(len(words)):
        if font.size(line+words[i]+' ')[0]<=width:
            line+=words[i]+' '
        else:
            lines.append(font.render(line,True,textColor))
            line=''
            line+=words[i]+' '
            i-=2
    if line!='':
        lines.append(font.render(line,True,textColor))
    return lines
#print(autoWrap('This is an incredible test i sure hope it doesn\'t go wrong',170,pygame.font.SysFont('comic sans ms',12),'white'))

if __name__=='__main__':
    print('This script doesn\'t work on its own. Import it into a project to use the functions and classes defined here')
else:
    print('Using PyEngine v0.4.1 APLHA') 