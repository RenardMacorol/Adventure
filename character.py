class Character:
    def __init__(self,name="Unkown",classType="person",health=0,strength=0,defense=0,intelligence=0, attackSpeed=0,isNpc=True):
        self.name = name
        self.classType = classType
        self.health = health
        self.strength = strength
        self.defense = defense
        self.intelligence = intelligence
        self.attackSpeed = attackSpeed
        self.isNpc = isNpc
    def ability1(self, Character):
        self.noSkill()
    def ability2(self, Character):
        self.noSkill()
    def ability3(self, Character):
        self.noSkill()
    def ability4(self, Character):
        self.noSkill()
    def noSkill(self):
        print("No Skill in this slot")
    def cooldownCheck(self):
        return
       
