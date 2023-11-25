import json
from customtkinter import *
from tkinter import *
itemType=None
def create(type):
    global itemType,itemName,itemSprite,blockSprite,maxStackSize
    itemType=tab.get()
    if type=='item':
        items.append({'Name':itemName.get(),'Id':len(items),'MaxStackSize':int(maxStackSize.get()),'Sprite':itemSprite.get(),'Type':itemType})
        idInd.configure(True,text=f'This item\'s id will be: {len(items)}')
        print(items)
    elif type=='block':
        blocks.append({'Name':itemName.get(),'Id':len(items),'MaxStackSize':int(maxStackSize.get()),'Sprite':itemSprite.get(),'BlockSprite':blockSprite.get(),'Type':itemType})
        idInd.configure(True,text=f'This item\'s id will be: {len(items)}')
        print(items)
    elif type=='tool':
        #items.append({'Name':itemName.get(),'Id':len(items),'Sprite':itemSprite.get(),'Type':itemType})
        idInd.configure(True,text=f'This item\'s id will be: {len(items)}')
        print(items)
    elif type=='recipe':
        #print('WIP DO NOT USE')
        for slot in recipe:
            if slot.get()=='':
                realRecipe.append(None)
            else:
                realRecipe.append(int(slot.get()))
        recipes.append({"Id":len(recipes),"Name":recipeName.get(),"Recipe":realRecipe,"Output":int(output.get()),"Shapeless":shapeless.get(),"Count":int(count.get())})
        recIdInd.configure(True,text=f'This recipe\'s id will be: {len(recipes)}')
        print(recipes)
def saveItem():
    with open('data\\items.json','w') as f:
        json.dump(items,f)
def saveBlock():
    with open('data\\blocks.json','w') as f:
        json.dump(blocks,f)
def saveRecipe():
    with open('data\\recipes.json','w') as f:
        json.dump(recipes,f)
def itemList():
    itemListWin=CTk()
    itemListWin.title('Item List')
    itemListWin.geometry('200x600')
    CTkLabel(itemListWin,text='Name').grid(column=1,row=0)
    CTkLabel(itemListWin,text='Icon').grid(column=2,row=0,padx=30)
    CTkLabel(itemListWin,text='Id').grid(column=3,row=0)
    for item in items:
        #print('items\\'+item['Sprite'])
        CTkLabel(itemListWin,text=item['Name'],anchor='w').grid(column=1,row=item['Id']+1)
        CTkLabel(itemListWin,image=PhotoImage(master=itemListWin,file='items\\'+item['Sprite']),text=None,anchor='w').grid(column=2,row=item['Id']+1)
        CTkLabel(itemListWin,text=item['Id'],anchor='w').grid(column=3,row=item['Id']+1)
    itemListWin.mainloop()
mainWin=CTk()
mainWin.title('Item Creation Tool')
mainWin.geometry('400x450')
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
CTkEntry(recFrame,textvariable=recipe[1],width=20).grid(row=1,column=2)
CTkEntry(recFrame,textvariable=recipe[2],width=20).grid(row=1,column=3)
CTkEntry(recFrame,textvariable=recipe[3],width=20).grid(row=2,column=1)
CTkEntry(recFrame,textvariable=recipe[4],width=20).grid(row=2,column=2)
CTkEntry(recFrame,textvariable=recipe[5],width=20).grid(row=2,column=3)
CTkEntry(recFrame,textvariable=recipe[6],width=20).grid(row=3,column=1)
CTkEntry(recFrame,textvariable=recipe[7],width=20).grid(row=3,column=2)
CTkEntry(recFrame,textvariable=recipe[8],width=20).grid(row=3,column=3)

CTkEntry(recFrame,textvariable=output,width=20).grid(row=2,column=5)
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
#Create Button
CTkButton(tab.tab('Item'),text='Create',command=lambda:create('item')).pack()
CTkButton(tab.tab('Block'),text='Create',command=lambda:create('block')).pack()
CTkButton(tab.tab('Tool'),text='Create',command=lambda:create('tool')).pack()
CTkButton(tab.tab('Recipe'),text='Create',command=lambda:create('recipe')).pack()
#Id Indicator
idInd=CTkLabel(tab.tab('Item'),text=f'This item\'s id will be: {len(items)}')
idInd.pack()
recIdInd=CTkLabel(tab.tab('Recipe'),text=f'This recipe\'s id will be: {len(recipes)}')
recIdInd.pack()
#Save Button
CTkButton(tab.tab('Item'),text='Save to JSON',command=saveItem).pack()
CTkButton(tab.tab('Block'),text='Save to JSON',command=saveBlock).pack()
CTkButton(tab.tab('Recipe'),text='Save to JSON',command=saveRecipe).pack()
tab.pack()
CTkButton(mainWin,text='View all items',command=itemList).pack()
mainWin.mainloop()