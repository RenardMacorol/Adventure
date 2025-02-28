from damageCounter import DamageCounter
from character import Character 
class Mage(Character):
    def __init__(self):
        super().__init__("Holmes","Mage",300,5,20,20,20,False)
        self.fireballCooldown = 2
    def ability1(self, Character):
        self.fireball(Character)
    def fireball(self,Character):
        if self.fireballCooldown== 0:
            self.fireballCooldown =2
            DamageCounter.dmg(Character,self,self.strength*self.intelligence,self.name)
        else:
            print(f"You can't hit this turn: {self.fireballCooldown} left before you can use this")
            self.fireballCooldown-=1
    def cooldownCheck(self):
        return self.fireballCooldown
