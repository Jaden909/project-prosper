class Enemy:
    def __init__(self,ai,sprite,name,biomes,spawnChance,moveDelay):
        self.x=random.choice(range(512))
        self.y=random.choice(range(512))
        self.rect=pygame.Rect((self.x,self.y),(64,64))
        self.ai=compile(open(PurePath(ai)).read(),PurePath(ai),'exec')
        self.sprite=pygame.image.load(PurePath(sprite))
        self.name=name
        self.biomes=biomes
        self.spawnChance=spawnChance
        self.delay=0
        self.moveDelay=moveDelay
        enemies.append(self)
    def update(self):
        global currentEnemy
        currentEnemy=self
        exec(self.ai,globals())
        screen.blit(self.sprite,self.rect)
    def spawn(self):
        if random.choice(range(1001))<self.spawnChance*10:
            activeEnemies.append(self)
