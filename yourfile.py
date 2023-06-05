# import random

# total_rounds = 0

# class GameEntity:
#     def __init__(self, name, health, damage) -> None:
#         self.__name = name
#         self.__health = health
#         self.__damage = damage

#     @property
#     def name(self):
#         return self.__name
    
#     @property
#     def health(self):
#         return self.__health

#     @health.setter
#     def health(self, value):
#         if value < 0:
#             self.__health = 0
#         else:
#             self.__health = value

#     @property
#     def damage(self):
#         return self.__damage

#     @damage.setter
#     def damage(self, value):
#         self.__damage = value
    
#     def __str__(self) -> str:
#         return f'{self.name} health: {self.health} [{self.damage}]'
    

# class Boss(GameEntity):
#     def __init__(self, name, health, damage) -> None:
#         super().__init__(name, health, damage)
    
#     def hit(self, heroes: list):
#         for hero in heroes:
#             if hero.health > 0 and self.health > 0:
#                 hero.health -= self.damage

#     def __str__(self) -> str:
#         return "BOSS " + super().__str__()

# class Hero(GameEntity):
#     def __init__(self, name, health, damage, super_ability) -> None:
#         super().__init__(name, health, damage)
#         self.__super_ability = super_ability

#     @property
#     def super_ability(self):
#         return self.__super_ability

#     @super_ability.setter
#     def super_ability(self, value):
#         self.__super_ability = value
    
#     def hit(self, boss: Boss):
#         if boss.health > 0 and self.health > 0:
#             boss.health -= self.damage

#     def apply_super_power(self, boss: Boss, heroes: list):
#         pass


# class Warior(Hero):
#     def __init__(self, name, health, damage) -> None:
#         super().__init__(name, health, damage, "CRITICAL DAMAGE")
    

#     def apply_super_power(self, boss: Boss, heroes: list):
#         coef = random.randint(0, 5)
#         boss.health -= self.damage * coef
#         print(f"Warrior {self.name} hits criticaly: {self.damage * coef}")


# class Medic(Hero):
#     def __init__(self, name, health, damage, heal_point) -> None:
#         super().__init__(name, health, damage, "HEAL")
#         self.__heal_point = heal_point

#     def apply_super_power(self, boss: Boss, heroes: list):
#         print(f"Medic: {self.name} heal {self.__heal_point}")
#         for hero in heroes:
#             if hero.health > 0 and hero != self:
#                 hero.health += self.__heal_point


# class Mag(Hero):
#     def __init__(self, name, health, damage) -> None:
#         super().__init__(name, health, damage, "BOOST")

#     def apply_super_power(self, boss: Boss, heroes: list):
#         boost_point = random.choice([5, 10, 15])
#         print(f"Mag: {self.name} boost {boost_point}")
#         for hero in heroes:
#             if hero.health > 0 and hero != self:
#                 hero.damage += boost_point

# class Thor(Hero):
#     def __init__(self, name, health, damage) -> None:
#         super().__init__(name, health, damage, "STUN")

#     def hit(self, boss: Boss):
#         if boss.health > 0 and self.health > 0:
#             if random.randint(0, 20) < self.damage:
#                 print(f"Thor оглушил босса {boss.name}!")
#             else:
#                 boss.health -= self.damage


# class Druid(Hero):
#     def __init__(self, name, health, damage) -> None:
#         super().__init__(name, health, damage, "SUMMON")

#     def summon_ally(self, boss: Boss, heroes: list):
#         ally = random.choice(["ANGEL", "RAVEN"])

#         if ally == "ANGEL":
#             self.apply_angel(heroes)
#         elif ally == "RAVEN":
#             self.apply_raven(boss)

#     def apply_angel(self, heroes: list):
#         n = random.randint(5, 15)  
#         for hero in heroes:
#             if isinstance(hero, Druid):
#                 hero.heal_point += n
#         print(f"Druid призвал ангела! Тору добавлена {n} единиц усиления исцеления.")

#     def apply_raven(self, boss: Boss):
#         if boss.health < 0.5 * boss.max_health:
#             damage_increase = boss.damage * 0.5  
#             boss.damage += damage_increase
#             print(f"Druid призвал ворона! Урон босса увеличен на 50%: {damage_increase}.")

# def is_game_finished(boss: Boss, heroes):
#     if boss.health <= 0:
#         print("Heroes WON!")
#         return True

#     all_heroes_dead = True
#     for hero in heroes:
#         if hero.health > 0:
#             all_heroes_dead = False
    
#     if all_heroes_dead:
#         print("Boss WON!")

#     return all_heroes_dead
    

# def print_statistic(boss: Boss, heroes):
#     print(f"___________{total_rounds} Round___________")
#     print(boss)
#     for hero in heroes:
#         print(hero)


# def heroes_power(boss: Boss, heroes: list):
#     boss_ability = random.choice(["CRITICAL DAMAGE", "HEAL", "BOOST"])
#     print(f"Boss {boss.name} blocked {boss_ability}")
#     for hero in heroes:
#         if boss_ability != hero.super_ability and boss.health > 0 and hero.health > 0:
#             hero.apply_super_power(boss, heroes)


# def play_round(boss: Boss, heroes: list):
#     print_statistic(boss, heroes)
#     global total_rounds
#     total_rounds += 1
#     boss.hit(heroes)
#     for hero in heroes:
#         hero.hit(boss)
#     heroes_power(boss, heroes)

# def main():
#     boss = Boss("Nurbolot", 2000, 50)

#     warrior = Warior("Ashat", 260, 10)
#     warrior_2 = Warior("Kurmanbek", 290, 20)
#     medic = Medic("Islam", 220, 5, 15)
#     medic_asistent = Medic("Janysh", 240, 10, 5)
#     magic = Mag("Magomed", 290, 20)
#     thor = Thor("Thor", 280, 20)
#     druid = Druid("Druid", 240, 20)

#     heroes = [warrior, medic, medic_asistent, magic, warrior_2, thor, druid]

#     while not is_game_finished(boss, heroes):
#         play_round(boss, heroes)
    
#     print_statistic(boss, heroes)

# main()







































# # СУБД - Система Управления Базой Данных
# # SQL - Structured Query Language
# # NoSql - Not Only Structured Query Language
# # CRUD - Create Reed Update Delete

import sqlite3


def create_connection(db_name):
    connection = sqlite3.connect(db_name)
    return connection


def create_table(conn, sql):
    cursor = conn.cursor()
    cursor.execute(sql)


def create_student(conn, student: tuple):
    sql = '''INSERT INTO students
     (full_name, mark, hobby, birth_date, is_married) 
     VALUES (?, ?, ?, ?, ?);'''
    cursor = conn.cursor()
    cursor.execute(sql, student)
    conn.commit()


# def delete_student(conn, id: int):
#     sql = '''DELETE FROM students WHERE id = ?'''
#     cursor = conn.cursor()
#     cursor.execute(sql, (id,))
#     conn.commit()


# def update_students_mark(conn, id, new_mark):
#     sql = '''UPDATE students SET mark = ? WHERE id = ?'''
#     cursor = conn.cursor()
#     cursor.execute(sql, (new_mark, id))
#     conn.commit()


def select_all_students(conn):
    sql = '''SELECT AVG(mark), is_married FROM students GROUP BY is_married;'''
    cursor = conn.cursor()
    rows = cursor.execute(sql).fetchall()
    for row in rows:
        print(row)
    



sql_create_table = '''
CREATE TABLE IF NOT EXISTS students (
id INTEGER PRIMARY KEY AUTOINCREMENT,
full_name VARCHAR (200) NOT NULL,
mark DOUBLE (5, 2) NOT NULL DEFAULT 0.0,
hobby TEXT DEFAULT NULL,
birth_date DATE NOT NULL,
is_married BOOLEAN DEFAULT FALSE
);
'''

connection = create_connection("school.db")
if connection:
    print("Database connected!")
    create_table(connection, sql_create_table)
    select_all_students(connection)

#     update_students_mark(connection, 3, 100)

#     delete_student(connection, 2)

#     create_student(connection, ("Esenbek", 30.23, None, "2003-06-08", False))
#     create_student(connection, ("Mark Daniels", 77.12, "Football", "1999-01-02", False))
#     create_student(connection, ("Alex Brilliant", 77.12, None, "1989-12-31", True))
#     create_student(connection, ("Diana Julls", 99.3, "Tennis", "2005-01-22", True))
#     create_student(connection, ("Michael Corse", 100.0, "Diving", "2001-09-17", True))
#     create_student(connection, ("Jack Moris", 50.2, "Fishing and cooking", "2001-07-12", True))
#     create_student(connection, ("Viola Manilson", 41.82, None, "1991-03-01", False))
#     create_student(connection, ("Joanna Moris", 100.0, "Painting and arts", "2004-04-13", False))
#     create_student(connection, ("Peter Parker", 32.0, "Travelling and bloging", "2002-11-28", False))
#     create_student(connection, ("Paula Parkerson", 77.09, None, "2001-11-28", True))
#     create_student(connection, ("George Newel", 93.0, "Photography", "1981-01-24", True))
#     create_student(connection, ("Miranda Alistoun", 87.55, "Playing computer games", "1997-12-22", False))
#     create_student(connection, ("Fiona Giordano", 66.12, "Driving fast", "1977-01-15", True))


#     print("Succes!")