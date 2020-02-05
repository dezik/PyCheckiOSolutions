# Taken from mission Army Battles

class Army:
    def __init__(self):
        self.units = []

    def add_units(self, warrior_type, count: int):
        self.units.extend([warrior_type() for _ in range(count)])

    def get_unit(self):
        if self.units[0].is_alive:
            return self.units[0]
        else:
            self.units.pop(0)
            if self.units:
                return self.units[0]

    def has_units(self):
        return len(self.units) > 0


class Battle:
    def fight(self, first_army: Army, second_army: Army) -> bool:
        winner = True
        while first_army.has_units() and second_army.has_units():
            first = first_army.get_unit()
            second = second_army.get_unit()
            if first is None:
                return False
            if second is None:
                return True
            winner = fight(first, second)
        return winner


class Warrior:

    def __init__(self):
        self.health = 50
        self.attack = 5

    @property
    def is_alive(self) -> bool:
        return self.health > 0


class Knight(Warrior):

    def __init__(self):
        super().__init__()
        self.attack = 7


def fight(unit_1: Warrior, unit_2: Warrior):
    first, second = unit_1, unit_2
    while unit_1.is_alive and unit_2.is_alive:
        unit_2.health -= unit_1.attack
        unit_1, unit_2 = unit_2, unit_1
    return (first is unit_1 and unit_1.is_alive) or (first is unit_2 and unit_2.is_alive)


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    
    #fight tests
    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()
    bob = Defender()
    mike = Knight()
    rog = Warrior()
    lancelot = Defender()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False
    assert fight(bob, mike) == False
    assert fight(lancelot, rog) == True

    #battle tests
    my_army = Army()
    my_army.add_units(Defender, 1)
    
    enemy_army = Army()
    enemy_army.add_units(Warrior, 2)

    army_3 = Army()
    army_3.add_units(Warrior, 1)
    army_3.add_units(Defender, 1)

    army_4 = Army()
    army_4.add_units(Warrior, 2)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == False
    assert battle.fight(army_3, army_4) == True
    print("Coding complete? Let's try tests!")
