from character import Character 
from damageCounter import DamageCounter
class Archer(Character):
    def __init__(self):
        super().__init__("Orion","Archer",300,150,20,30,20,False)
        self.arrowCooldown = 4
    def ability1(self, Character):
        self.superArrow(Character)
    def superArrow(self,Character):
        if self.arrowCooldown== 0:
            self.arrowCooldown =3
            DamageCounter.dmg(Character,self,self.strength,self.name)
        else:
            print(f"You can't hit this turn: {self.arrowCooldown} left before you can use this")
            self.arrowCooldown-=1
    def cooldownCheck(self):
        return self.arrowCooldown
