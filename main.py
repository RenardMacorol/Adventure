##Hybrid Character Creation
from enemy import Enemy
from character import Character
from archer import Archer
from swordsman import SwordsMan
from mage import Mage
from overlord import OverLord
from damageCounter import DamageCounter
class Game:
    player = Character()
    def __init__(self):
        print("Welcome to the the game")
    def chooseCharacter(self):
        choice =0
        while(choice == 0):
            print("Please Choose a Character:")
            print("1. Swordsman")
            print("2. Archer")
            print("3. Mage")
            print("4. Lich")
            choice = int(input())
            if(choice == 1):
                self.player = SwordsMan()
                print("Looks like you chose Swordsman get ready ")
            elif(choice == 2):
                self.player = Archer()
                print("Looks like you chose Archer get ready ")
            elif(choice == 3):
                self.player = Mage()
                print("Looks like you chose Mage get ready ")
            elif(choice == 4):
                self.player = OverLord()
                print("Looks like you chose Overload get ready ")
    def spawnEnemy(self):
        choice = 0
        enemy = Enemy()
        print("There is enemy now kill it")
        while not enemy.isDead :
            if(self.player.health <=0):
                break;
            print("Choose Ability to Defeat it")
            choice = int(input())
            if(self.player.health > 0):
                if(choice==1):
                    self.player.ability1(enemy)
                    if enemy.isDead:
                        break;
                elif(choice==2):
                    self.player.ability2(enemy)
                    if enemy.isDead:
                        break;
                elif(choice==3):
                    self.player.ability3(enemy)
                    if enemy.isDead:
                        break;
                elif(choice==4):
                    self.player.ability4(enemy)
                    if enemy.isDead:
                        break;
                else:
                    print("Invalid Key please click Enter Only 1-4")
                print(self.player.cooldownCheck())
            DamageCounter.dmg(self.player,enemy,enemy.strength,enemy.name)
       
newGame  = Game()
newGame.chooseCharacter()
newGame.spawnEnemy()