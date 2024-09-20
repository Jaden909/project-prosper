class Recipe:
    def __init__(self,recipeId):
        self.recipeId=recipeId
        self.data=recipes[self.recipeId]
        self.name=self.data['Name']
        self.recipe=self.data['Recipe']
        self.output=self.data['Output']
        self.shapeless=self.data['Shapeless']
        self.count=self.data['Count']
        self.type=self.data['type']
        self.requires=self.data['Requires']
        self.items=[]
        self.craftItems=[]
    def checkRecipe(self,craftingInv:list):
        if self.requires is not None:
            if researches[self.requires]:
                self.items.clear()
                self.craftItems.clear()
                if not self.shapeless:
                    if craftingInv==self.recipe:
                        return True
                    return False
                elif self.shapeless:
                    for item in self.recipe:
                        if item is not None:
                            self.items.append(item)
                    for item in craftingInv:
                        if item is not None:
                            self.craftItems.append(item)
                    self.items.sort()
                    self.craftItems.sort()
                    if self.items==self.craftItems:
                        return True
                    return False
            return False
        else:
            if not self.shapeless:
                if craftingInv==self.recipe:
                    return True
                return False
            elif self.shapeless:
                for item in self.recipe:
                    if item is not None:
                        self.items.append(item)
                for item in craftingInv:
                    if item is not None:
                        self.craftItems.append(item)
                self.items.sort()
                self.craftItems.sort()
                if self.items==self.craftItems:
                    return True
                return False
        return False