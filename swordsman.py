from character import Character 
from damageCounter import DamageCounter

class SwordsMan(Character):
    def __init__(self):
        super().__init__("Razeal","SwordsMan",300,30,50,30,20,False)
        self.slashCoolDown = 0
    def ability1(self,Character):
        self.slash(Character)
    def slash(self,Character):
        if self.slashCoolDown == 0:
            self.slashCoolDown =1
            DamageCounter.dmg(Character,self,self.strength,self.name)
        else: 
            print(f"You can't hit this turn: {self.slashCoolDown} left before you can use this")
            self.slashCoolDown-=1
    def cooldownCheck(self):
        return self.slashCoolDown
