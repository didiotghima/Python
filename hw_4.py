import random 
 
total_rounds = 0 

class Game:
    def __init__(self, name, health, damage, super_ability):
        self.__name = name 
        self.__health = health
        self.__damage = damage
        self.__super_ability = super_ability

    @property
    def name(self):
        return self.__name
    
    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        if value < 0:
            self.__health = 0
        else:
            self.__health = value

    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, value):
        self.__damage = value

    @property
    def super_ability(self):
        return self.__super_ability
    
    def __str__(self):
        return f'{self.name} health: {self.health} [{self.damage}]'
    
class Boss(Game):
    def __init__(self, name, health, damage, super_ability):
        super().__init__(name, health, damage, super_ability)

    def hit(self, heroes: list):
        for hero in heroes:
            if hero.health > 0 and self.health > 0:
                hero.health -= self.damage

    def __str__(self):
        return "Boss " + super().__str__()
    
class Hero(Game):
    def __init__(self, name, health, damage, super_ability):
        super().__init__(name, health, damage, super_ability)

    def hit(self, boss: Boss):
        if boss.health > 0 and self.health > 0:
            boss.health -= self.damage

    def apply_super_power(self, boss: Boss, heroes: list):
        pass

class Berserk(Hero):
    def __init__(self, name, health, damage) -> None:
        super().__init__(name, health, damage, "Part Damage")
    
    def apply_super_power(self, boss: Boss, heroes: list):
        boss.health -= boss.damage
        print(f"Warrior {self.name} hits Part Damage : {boss.damage}\n")    

class Hacker(Hero):
    def __init__(self, name, health, damage) -> None:
        super().__init__(name, health, damage, "HACK")

    def hack_boss(self, boss: Boss, heroes: list):
        health_stolen = random.randint(50, 150)  
        boss.health -= health_stolen

        hero_to_heal = random.choice(heroes)  
        hero_to_heal.health += health_stolen

        print(f"Hacker {self.name} украл {health_stolen} здоровья у босса {boss.name} и передал его герою {hero_to_heal.name}.")


def is_game_finished(boss: Boss, heroes: list):
    if boss.health <= 0:
        print("Heroes WON!")
        return True

    all_heroes_dead = True
    for hero in heroes:
        if hero.health > 0:
            all_heroes_dead = False
    
    if all_heroes_dead:
        print("Boss WON!")

    return all_heroes_dead
    
def print_statistic(boss: Boss, heroes: list):
    print(f"___________{total_rounds} Round___________")
    print(boss)
    for hero in heroes:
        print(hero)

def heroes_power(boss: Boss, heroes: list):
    boss_ability = random.choice(["Part Damage", "HACK"])
    print(f"Boss {boss.name} blocked {boss_ability}")
    for hero in heroes:
        if boss_ability != hero.super_ability and boss.health > 0 and hero.health > 0:
            hero.apply_super_power(boss, heroes)


def play_round(boss: Boss, heroes: list):
    global total_rounds
    total_rounds += 1
    boss.hit(heroes)
    for hero in heroes:
        hero.hit(boss)
    heroes_power(boss, heroes)

def main():
    boss = Boss("Thanos", 2000, 90, "porfekt")

    
    allies1 = Berserk("Thor", 1100, 50)
    allies2 = Hacker("Druid", 1300, 0)
 
    heroes = [allies1, allies2]
     
    while not is_game_finished(boss, heroes):
        print_statistic(boss, heroes)
        play_round(boss, heroes)

main()
