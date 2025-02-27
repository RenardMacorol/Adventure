from character import Character 
class Enemy(Character):
    def __init__(self):
        super().__init__("Roscaht","Demon",75,100,5,50,50,True)
        self.isDead = False
    