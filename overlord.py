
from archer import Archer
from character import Character
from mage import Mage
from swordsman import SwordsMan 
from character import Character 

class OverLord(Mage,Archer,SwordsMan):
    def __init__(self):
        name = "Lich"
        classType = "Over Lord"
        health = 300
        strength = 75
        defense = 55 
        intelligence = 150
        attackSpeed = 250
        Character.__init__(self,name,classType,health,strength,defense,intelligence, attackSpeed,False)
        self.fireballCooldown = 0
        self.arrowCooldown = 0
        self.slashCoolDown = 0
    def ability1(self, Character):
        self.slash(Character)
    def ability2(self, Character):
        self.superArrow(Character)
    def ability3(self, Character):
        self.fireball(Character)
    def cooldownCheck(self):
        return "firball :"+ str(self.fireballCooldown) + ", arrow "+ str(self.arrowCooldown)+ ",slash" +str(self.slashCoolDown) 

