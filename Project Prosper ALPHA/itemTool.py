#import projectprosper
import json
from customtkinter import *
from tkinter import *
from pathlib import PurePath
itemType=None
tags={}
#ADD NEW TYPE PARAMETER TO RECIPES
def create(type):
    global itemType,itemName,itemSprite,blockSprite,maxStackSize
    itemType=tab.get()
    if type=='item':
        items.append({'Name':itemName.get(),'Id':len(items),'MaxStackSize':int(maxStackSize.get()),'Sprite':itemSprite.get(),'Type':itemType,'Tags':tags})
        idInd.configure(True,text=f'This item\'s id will be: {len(items)}')
        print(items)
    elif type=='block':
        blocks.append({'Name':itemName.get(),'Id':len(items),'MaxStackSize':int(maxStackSize.get()),'Sprite':itemSprite.get(),'BlockSprite':blockSprite.get(),'Type':itemType})
        idInd.configure(True,text=f'This item\'s id will be: {len(items)}')
        print(items)
    elif type=='tool':
            
        items.append({'Name':itemName.get(),'Id':len(items),'MaxStackSize':1,'Sprite':itemSprite.get(),'Type':itemType,'Tags':{'durability':durability.get(),'harvestLevel':harvestLevel.get(),'lscript':lscript.get() if lscript.get()!="" else None,'rscript':rscript.get() if rscript.get()!="" else None}})
        idInd.configure(True,text=f'This item\'s id will be: {len(items)}')
        print(items)
    elif type=='recipe':
        #print('WIP DO NOT USE')
        for slot in recipe:
            if slot.get()=='':
                realRecipe.append(None)
            else:
                realRecipe.append(int(slot.get()))
        recipes.append({"Id":len(recipes),"Name":recipeName.get(),"Recipe":realRecipe.copy(),"Output":int(output.get()),"Shapeless":shapeless.get(),"Count":int(count.get()),"Requires":requires.get() if requires.get()>=0 else None,'type':'crafting'})
        recIdInd.configure(True,text=f'This recipe\'s id will be: {len(recipes)}')
        realRecipe.clear()
        print(recipes)
def saveItem():
    with open('data\\items.json','w') as f:
        json.dump(items,f)
    print('Saved sucessfully')
def saveBlock():
    with open('data\\blocks.json','w') as f:
        json.dump(blocks,f)
    print('Saved sucessfully')
def saveRecipe():
    with open('data\\recipes.json','w') as f:
        json.dump(recipes,f)
    print('Saved sucessfully')    
def itemList():
    itemListWin=CTk()
    itemListWin.title('Item List')
    itemListWin.geometry('200x600')
    CTkLabel(itemListWin,text='Name').grid(column=1,row=0)
    CTkLabel(itemListWin,text='Icon').grid(column=2,row=0,padx=30)
    CTkLabel(itemListWin,text='Id').grid(column=3,row=0)
    currentColumn=0
    for item in items:
        #print('items\\'+item['Sprite'])
        CTkLabel(itemListWin,text=item['Name'],anchor='w').grid(column=1+4*currentColumn,row=item['Id']+1-20*currentColumn)
        CTkLabel(itemListWin,image=PhotoImage(master=itemListWin,file='items\\'+item['Sprite']),text=None,anchor='w').grid(column=2+4*currentColumn,row=item['Id']+1-20*currentColumn)
        CTkLabel(itemListWin,text=item['Id'],anchor='w').grid(column=3+4*currentColumn,row=item['Id']+1-20*currentColumn,padx=10)
        print(item['Id']+1)
        if (item['Id']+1)%20==0:
            print('briuh')
            currentColumn+=1
    itemListWin.mainloop()
def tagEditor():
    def newTag():
        names.append(CTkEntry(editorFrame,placeholder_text='Tag Name...'))
        values.append(CTkEntry(editorFrame,placeholder_text='Tag Value...'))
        names[-1].grid(row=len(names)-1,column=0)
        values[-1].grid(row=len(names)-1,column=1)
    def allTags():
        tagListWin=CTk()
        tagListWin.title('Tag List')
        tagListWin.geometry('800x400')
        
        
        tagFrame=CTkFrame(tagListWin)
        topTagFrame=CTkFrame(tagListWin,height=25,width=tagFrame.winfo_reqwidth()*2)
        topTagFrame.grid_propagate(False)
        CTkLabel(tagFrame,text='All Tags').grid(row=0,column=0)
        CTkLabel(tagFrame,text='Description').grid(row=0,column=2,padx=25)
        currentRow=1
        for tag in json.load(open(PurePath('data','tags.json'))):
            CTkLabel(tagFrame,text=tag['Name'],).grid(row=currentRow,column=0)
            CTkLabel(tagFrame,text=tag['Desc']).grid(row=currentRow,column=2)
            currentRow+=1
        #print(tagFrame.winfo_reqwidth())
        
        #CTkLabel(topTagFrame,text='All Tags').grid(row=0,column=0)
        #CTkLabel(topTagFrame,text='Description').grid(row=0,column=2,padx=25)
        #topTagFrame.pack()
        tagFrame.pack()
        tagListWin.mainloop()
    def saveTags():
        global tags
        
        for i in range(len(names)):
            #Try to convert value to other types
            try: #Try to int
                tags[names[i].get()]=int(values[i].get())
            except:
                if ',' in values[i].get(): #Detect multiple values
                    try: #Try to int values
                        tags[names[i].get()]=[int(v) for v in values[i].get() if v !=',']
                    except: #Just raw values
                        tags[names[i].get()]=[v for v in values[i].get() if v !=',']
                else: #Raw string
                    tags[names[i].get()]=values[i].get()
        print(tags)
        tagEditWin.destroy()
    names=[]
    values=[]
    tagEditWin=CTk()
    tagEditWin.title('Tag Editor')
    tagEditWin.geometry('400x400')
    CTkLabel(tagEditWin,text='Tag Creator').pack()

    editorFrame=CTkFrame(tagEditWin)
    names.append(CTkEntry(editorFrame,placeholder_text='Tag Name...'))
    values.append(CTkEntry(editorFrame,placeholder_text='Tag Value...'))
    names[-1].grid(row=0,column=0)
    values[-1].grid(row=0,column=1)
    editorFrame.pack()
    CTkButton(tagEditWin,text='New Tag',command=newTag).pack()
    CTkButton(tagEditWin,text='View Possible Tags',command=allTags).pack()
    CTkButton(tagEditWin,text='Save Tags',command=saveTags).pack(pady=10)


    
    tagEditWin.mainloop()
mainWin=CTk()
mainWin.title('Item Creation Tool')
mainWin.geometry('400x600')
items:list=json.load(open('data\\items.json'))
blocks=json.load(open('data\\blocks.json'))
recipes=json.load(open('data\\recipes.json'))
with open('data\\itemsBackup.json','w') as f:
    json.dump(items,f)
with open('data\\blocksBackup.json','w') as f:
    json.dump(blocks,f)
with open('data\\recipesBackup.json','w') as f:
    json.dump(recipes,f)
#SegmentedButton an TabView
realRecipe=[]
itemName=StringVar()
recipeName=StringVar()
maxStackSize=StringVar()
itemSprite=StringVar()
blockSprite=StringVar()
output=StringVar()
shapeless=BooleanVar()
count=StringVar()
durability=StringVar()
harvestLevel=StringVar()
lscript=StringVar()
rscript=StringVar()
requires=IntVar(value=-1)
recipe=[StringVar()for i in range(9)]
#print(recipe)
typeLabel=CTkLabel(mainWin,text='Item Type').pack()
tab=CTkTabview(mainWin,height=0)
tab.add('Item')
tab.add('Block')
tab.add('Tool')
tab.add('Recipe')
#Name Label
CTkLabel(tab.tab('Item'),text='Item Name').pack()
CTkLabel(tab.tab('Block'),text='Block Name').pack()
CTkLabel(tab.tab('Tool'),text='Tool Name').pack()
CTkLabel(tab.tab('Recipe'),text='Recipe Name').pack()
#Name Entry (1)
CTkEntry(tab.tab('Item'),textvariable=itemName).pack()
CTkEntry(tab.tab('Block'),textvariable=itemName).pack()
CTkEntry(tab.tab('Tool'),textvariable=itemName).pack()
CTkEntry(tab.tab('Recipe'),textvariable=recipeName).pack()
#Max Stack Size Label
CTkLabel(tab.tab('Item'),text='Max Stack Size').pack()
CTkLabel(tab.tab('Block'),text='Max Stack Size').pack()

#Max Stack Size Entry(2)
CTkEntry(tab.tab('Item'),textvariable=maxStackSize).pack()
CTkEntry(tab.tab('Block'),textvariable=maxStackSize).pack()

#Recipe Label
CTkLabel(tab.tab('Recipe'),text='Recipe (enter the ids of the component items and the output)').pack()
#Recipe Entries(2)
recFrame=CTkFrame(tab.tab('Recipe'))
CTkEntry(recFrame,textvariable=recipe[0],width=20).grid(row=1,column=1)
CTkEntry(recFrame,textvariable=recipe[1],width=20).grid(row=1,column=4)
CTkEntry(recFrame,textvariable=recipe[2],width=20).grid(row=1,column=6)
CTkEntry(recFrame,textvariable=recipe[3],width=20).grid(row=2,column=1)
CTkEntry(recFrame,textvariable=recipe[4],width=20).grid(row=2,column=4)
CTkEntry(recFrame,textvariable=recipe[5],width=20).grid(row=2,column=6)
CTkEntry(recFrame,textvariable=recipe[6],width=20).grid(row=3,column=1)
CTkEntry(recFrame,textvariable=recipe[7],width=20).grid(row=3,column=4)
CTkEntry(recFrame,textvariable=recipe[8],width=20).grid(row=3,column=6)

CTkEntry(recFrame,textvariable=output,width=20).grid(row=2,column=8)
recFrame.pack()
#Sprite Label
CTkLabel(tab.tab('Item'),text='Item Sprite Location').pack()
CTkLabel(tab.tab('Block'),text='Item Sprite Location').pack()
CTkLabel(tab.tab('Tool'),text='Item Sprite Location').pack()
#Sprite Entry (3)
CTkEntry(tab.tab('Item'),textvariable=itemSprite).pack()
CTkEntry(tab.tab('Block'),textvariable=itemSprite).pack()
CTkEntry(tab.tab('Tool'),textvariable=itemSprite).pack()
#Shapeless Label
#CTkLabel(tab.tab('Recipe'),text='Is the recipe shapeless?').pack()
#Tag edit
CTkButton(tab.tab('Item'),text='Edit Tags',command=tagEditor).pack(pady=5)
#Shapeless Switch(3)
CTkSwitch(tab.tab('Recipe'),text='Is the recipe shapeless?',variable=shapeless).pack()
#Block Sprite Label
CTkLabel(tab.tab('Block'),text='Placed Sprite Location').pack()
#Count Label
CTkLabel(tab.tab('Recipe'),text='How many output items are produced from this recipe?').pack()
#Count Entry
CTkEntry(tab.tab('Recipe'),textvariable=count).pack()
#Block Sprite Entry (4)
CTkEntry(tab.tab('Block'),textvariable=blockSprite).pack()
CTkLabel(tab.tab('Recipe'),text='What research does this recipe require? (leave -1 for None)').pack()
CTkEntry(tab.tab('Recipe'),textvariable=requires).pack()
#Tool Durability
CTkLabel(tab.tab('Tool'),text='How many durability points does this tool have?').pack()
CTkEntry(tab.tab('Tool'),textvariable=durability).pack()
#Tool Harvest Level
CTkLabel(tab.tab('Tool'),text='What is this tool\'s harvest level? (0=hand,1=basic tool)').pack()
CTkEntry(tab.tab('Tool'),textvariable=harvestLevel).pack()
#Tool l script
CTkLabel(tab.tab('Tool'),text='What script should be called on left click?').pack()
CTkEntry(tab.tab('Tool'),textvariable=lscript).pack()
#Tool r script
CTkLabel(tab.tab('Tool'),text='What script should be called on right click?').pack()
CTkEntry(tab.tab('Tool'),textvariable=rscript).pack()
#Create Button
CTkButton(tab.tab('Item'),text='Create',command=lambda:create('item')).pack(pady=5)
CTkButton(tab.tab('Block'),text='Create',command=lambda:create('block')).pack(pady=5)
CTkButton(tab.tab('Tool'),text='Create',command=lambda:create('tool')).pack(pady=5)
CTkButton(tab.tab('Recipe'),text='Create',command=lambda:create('recipe')).pack(pady=5)
#Id Indicator
idInd=CTkLabel(tab.tab('Item'),text=f'This item\'s id will be: {len(items)}')
idInd.pack()
recIdInd=CTkLabel(tab.tab('Recipe'),text=f'This recipe\'s id will be: {len(recipes)}')
recIdInd.pack()
idInd=CTkLabel(tab.tab('Tool'),text=f'This tool\'s id will be: {len(items)}')
idInd.pack()
#Save Button
CTkButton(tab.tab('Item'),text='Save to JSON',command=saveItem).pack()
CTkButton(tab.tab('Block'),text='Save to JSON',command=saveBlock).pack()
CTkButton(tab.tab('Recipe'),text='Save to JSON',command=saveRecipe).pack()
CTkButton(tab.tab('Tool'),text='Save to JSON',command=saveItem).pack()
tab.pack()
CTkButton(mainWin,text='View all items',command=itemList).pack()
mainWin.mainloop()