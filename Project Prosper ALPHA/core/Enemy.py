class Enemy:
    def __init__(self,id):
        self.id=id
        self.data=enemyData[id]
        self.hbSize=self.data['HitboxSize']
        self.x=random.choice(range(512))
        self.y=random.choice(range(512))
        self.rect=pygame.Rect((self.x,self.y),self.hbSize)

        self.ai=compile(open(PurePath('ai',self.data['Ai'])).read(),PurePath('ai',self.data['Ai']),'exec')
        self.sprite=pygame.image.load(PurePath('Enemies',self.data['Image']))
        self.name=self.data['Name']
        self.biomes=self.data['Biomes']
        self.spawnChance=self.data['SpawnChance']
        self.delay=0
        self.moveDelay=self.data['MoveDelay']
        self.maxHp=self.data['MaxHP']
        self.hp=self.maxHp
        self.iFrames=20
        self.tileId=player.id
        self.extraData=self.data['Extra Data']
        self.drops=self.data['Drops']
        
    def update(self):
        global currentEnemy
        if self.tileId==player.id:
            currentEnemy=self
            exec(self.ai,globals())
            
            if not slashDone or not slashLDone:
                if currentItem['Item'] is not None:
                    if getItem(currentItem['Item']).type=='Tool':
                        if self.rect.colliderect(slashRect) and self.iFrames<=0:
                            self.hp-=getItem(currentItem['Item']).damage
                            self.iFrames=slashSpeed
                            print(self.iFrames)
                            if self.hp<=0:
                                 self.die()
            self.iFrames-=1
    def die(self):
        activeEnemies.remove(self)
        for item in self.drops:
            if random.choice(range(100))<item['Chance']:
                for i in range(random.choice(item['Amount'])):
                    droppedItems.append({"Type":item['Item'],"Position":self.rect})
    def spawn(self):

            activeEnemies.append(Enemy(self.id))
