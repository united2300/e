import random

class Player:
    def __init__(self):
        self.level = 1
        self.stats = {'ATK': 0.2, 'MATK': 0.2, 'RAN': 0.2, 'HP': 0.1, 'DEF': 0.1, 'EVA': 0.1, 'HEAL': 0.05, 'STE': 0.05, 'SPD': 0.05, 'STA': 0.05}
        self.calculate_power()

    def calculate_power(self):
        offensive = sum([self.stats['ATK'], self.stats['MATK'], self.stats['RAN']]) / 3
        defensive = sum([self.stats['HP'], self.stats['DEF'], self.stats['EVA']]) / 3
        support = sum([self.stats['HEAL'], self.stats['STE'], self.stats['SPD'], self.stats['STA']]) / 4
        self.power = offensive + defensive + support

    def level_up(self):
        self.level += 1
        self.stats = {stat: min(1.0, stat_value * 1.01) for stat, stat_value in self.stats.items()}
        self.calculate_power()

    def display_stats(self):
        print("Level:", self.level)
        print("Stats:")
        for stat, value in self.stats.items():
            print(f"{stat}: {value:.2f}")
        print("Power:", self.power)

class Enemy:
    def __init__(self, level):
        self.level = level
        self.power = level * random.uniform(0.8, 1.2)  # Randomness in enemy power

    def is_defeated(self, player):
        return player.power > self.power

class Dungeon:
    def __init__(self):
        self.floor = 1

    def generate_enemy(self):
        enemy_level = max(1, self.floor // 10)  # Enemies get stronger every 10 floors
        return Enemy(enemy_level)

    def clear_floor(self, player):
        enemy = self.generate_enemy()
        print("\n=== Enemy Encounter ===")
        print(f"Enemy Level: {enemy.level}")
        print("=======================")

        while True:
            print("\n1. Attack")
            print("2. Cast Magic")
            print("3. Use Ranged Attack")
            print("4. Flee")
            choice = input("Choose your action: ")

            if choice == "1":
                player_attack = player.stats['ATK'] * random.uniform(0.8, 1.2)
                enemy_attack = enemy.power * random.uniform(0.8, 1.2)
                if player_attack > enemy_attack:
                    print("You defeated the enemy!")
                    self.floor += 1
                    player.level_up()
                    break
                else:
                    print("You were defeated by the enemy.")
                    return False

            elif choice == "2":
                player_attack = player.stats['MATK'] * random.uniform(0.8, 1.2)
                enemy_attack = enemy.power * random.uniform(0.8, 1.2)
                if player_attack > enemy_attack:
                    print("You defeated the enemy with magic!")
                    self.floor += 1
                    player.level_up()
                    break
                else:
                    print("You were defeated by the enemy's magic.")
                    return False

            elif choice == "3":
                player_attack = player.stats['RAN'] * random.uniform(0.8, 1.2)
                enemy_attack = enemy.power * random.uniform(0.8, 1.2)
                if player_attack > enemy_attack:
                    print("You defeated the enemy with ranged attack!")
                    self.floor += 1
                    player.level_up()
                    break
                else:
                    print("You were defeated by the enemy's ranged attack.")
                    return False

            elif choice == "4":
                print("You fled from the enemy.")
                return False

            else:
                print("Invalid choice. Please choose again.")

class Shop:
    def __init__(self):
        self.weapons = {'Sword': 0.1, 'Staff': 0.1, 'Bow': 0.1}

    def buy_weapon(self, player, weapon):
        if weapon in self.weapons:
            player.stats['ATK'] += self.weapons[weapon]
            player.calculate_power()
            print(f"You bought {weapon}! Your attack has increased.")
        else:
            print("Invalid weapon choice.")

class MageBar:
    def __init__(self):
        self.spells = {'Fireball': 0.1, 'Heal': 0.1, 'Lightning': 0.1}

    def buy_spell(self, player, spell):
        if spell in self.spells:
            player.stats['MATK'] += self.spells[spell]
            player.calculate_power()
            print(f"You bought the spell {spell}! Your magic attack has increased.")
        else:
            print("Invalid spell choice.")

class RangerDen:
    def __init__(self):
        self.arrows = {'Iron Arrow': 0.1, 'Silver Arrow': 0.1, 'Magic Arrow': 0.1}

    def buy_arrow(self, player, arrow):
        if arrow in self.arrows:
            player.stats['RAN'] += self.arrows[arrow]
            player.calculate_power()
            print(f"You bought {arrow}! Your ranged attack has increased.")
        else:
            print("Invalid arrow choice.")

def main():
    player = Player()
    dungeon = Dungeon()
    shop = Shop()
    mage_bar = MageBar()
    ranger_den = RangerDen()

    while True:
        print("\n=== Main Menu ===")
        print("1. Explore Dungeon")
        print("2. Visit Shop")
        print("3. Visit Mage's Bar")
        print("4. Visit Ranger's Den")
        print("5. Display Player Stats")
        print("6. Quit")
        choice = input("Choose an option: ")

        if choice == "1":
            dungeon.clear_floor(player)

        elif choice == "2":
            print("\n=== Shop ===")
            print("1. Buy Sword (+0.1 ATK)")
            print("2. Buy Staff (+0.1 ATK)")
            print("3. Buy Bow (+0.1 ATK)")
            weapon_choice = input("Choose a weapon to buy: ")
            if weapon_choice in ['1', '2', '3']:
                shop.buy_weapon(player, list(shop.weapons.keys())[int(weapon_choice) - 1])
            else:
                print("Invalid choice.")

        elif choice == "3":
            print("\n=== Mage's Bar ===")
            print("1. Buy Fireball (+0.1 MATK)")
            print("2. Buy Heal (+0.1 MATK)")
            print("3. Buy Lightning (+0.1 MATK)")
            spell_choice = input("Choose a spell to buy: ")
            if spell
