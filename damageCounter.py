class DamageCounter:
    def dmg(hit,hitter,total,name):
        totalDmg= total - hit.defense
        if(totalDmg<=0):
            totalDmg =0
        hit.health-=totalDmg
        if not hitter.isNpc:
            print(f"You hit this enemy name {hit.name}")
            print(f"Damage Dealth {totalDmg}")
            if(hit.health<=0):
                print(f"You win {name}")
                hit.isDead = True
                return
        else:
            print(f"You been hit by {name}")
            print(f"Damage Dealth {totalDmg}")
            if(hit.health<=0):
                print(f"You Lose {hit.name}")
                return
        print(f"Damage Check {hit.health}")
