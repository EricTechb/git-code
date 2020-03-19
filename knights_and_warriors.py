class Warrior:
    def __init__(self):
        self.health = 50
        self.attack = 5

    def is_alive(self):
        return self.health > 0

    def __bool__(self):
        return self.is_alive()

class Knight(Warrior):
    def __init__(self):
        super().__init__()
        self.attack = 7

class Army:
    def __init__(self):
        self.units = []
    
    def add_unit(self, unit):
        self.units.append(unit)
    
    def is_existing(self):
        return any(self.units)

    def first_alive(self):
        for unit in self.units:
            if unit.is_alive():
                return unit

def fight(unit1, unit2):
    print(f"{unit1} is fighting {unit2}")
    if type(unit1) == Army:
        while unit1.is_existing() and unit2.is_existing():
            fight(unit1.first_alive(), unit2.first_alive())

        if unit1.is_existing():
            return unit1
        else:
            return unit2

    else:
        while unit1.is_alive() and unit2.is_alive():
            unit2.health -= unit1.attack
            if not unit2.is_alive():
                return unit1

            unit1.health -= unit2.attack
        
        if unit1.is_alive():
            return unit1
        else:
            return unit2


alice = Warrior()
clark = Warrior()
bruce = Knight()

reds = Army()
reds.add_unit(alice)
reds.add_unit(clark)
reds.add_unit(bruce)

xavier = Knight()
yasmin = Warrior()
zack = Knight()
zeus = Knight()

blues = Army()
blues.add_unit(xavier)
blues.add_unit(yasmin)
blues.add_unit(zack)
blues.add_unit(zeus)

print("Fighting.")
winner = fight(reds, blues)
if winner == reds:
    print("Reds win")
else:
    print("Blues win")