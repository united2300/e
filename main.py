import random

class Player:
    def __init__(self):
        self.level = 1
        self.stats = {'ATK': 0.2, 'MATK': 0.2, 'RAN': 0.2, 'HP': 0.1, 'DEF': 0.1, 'EVA': 0.1, 'HEAL': 0.05, 'STE': 0.05, 'SPD': 0.05, 'STA': 0.05}
        self.calculate_power()
        self.gold = 100

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
        print("=== Player Stats ===")
        print("Level:", self.level)
        print("Stats:")
        for stat, value in self.stats.items():
            print(f"{stat}: {value:.2f}")
        print("Power:", self.power)
        print("Gold:", self.gold)
        print("====================")

    def buy_item(self, item, cost):
        if self.gold >= cost:
            self.gold -= cost
            if item == "Weapon":
                self.stats['ATK'] += 0.1
            elif item == "Magic Book":
                self.stats['MATK'] += 0.1
            elif item == "Arrows":
                self.stats['RAN'] += 0.1
            print(f"You bought {item}!")
            self.calculate_power()
        else:
            print("Not enough gold!")

class Enemy:
    def __init__(self, level):
        self.level = level
        self.stats = {'ATK': 0.2, 'MATK': 0.2, 'RAN': 0.2, 'HP': 0.1, 'DEF': 0.1, 'EVA': 0.1, 'HEAL': 0.05, 'STE': 0.05, 'SPD': 0.05, 'STA': 0.05}
        self.calculate_power()

    def calculate_power(self):
        offensive = sum([self.stats['ATK'], self.stats['MATK'], self.stats['RAN']]) / 3
        defensive = sum([self.stats['HP'], self.stats['DEF'], self.stats['EVA']]) / 3
        support = sum([self.stats['HEAL'], self.stats['STE'], self.stats['SPD'], self.stats['STA']]) / 4
        self.power = offensive + defensive + support

class Dungeon:
    def __init__(self):
        self.floor = 1

    def generate_enemy(self, player_level):
        enemy_level = max(1, player_level // 10)  # Enemies get stronger every 10 levels
        enemy = Enemy(enemy_level)
        return enemy

    def clear_floor(self, player):
        enemy = self.generate_enemy(player.level)
        print("\n=== Enemy Stats ===")
        print(f"Level: {enemy.level}")
        print("Enemy Power:", enemy.power)
        print("===================")

        while True:
            print("\n1. Normal Attack")
            print("2. Magic Attack")
            print("3. Ranged Attack")
            choice = input("Choose your action: ")

            if choice == "1":
                damage = player.stats['ATK'] * random.uniform(0.8, 1.2)
                print("You perform a normal attack, dealing", damage, "damage to the enemy!")
                break
            elif choice == "2":
                damage = player.stats['MATK'] * random.uniform(0.8, 1.2)
                print("You cast a magic attack, dealing", damage, "damage to the enemy!")
                break
            elif choice == "3":
                damage = player.stats['RAN'] * random.uniform(0.8, 1.2)
                print("You shoot a ranged attack, dealing", damage, "damage to the enemy!")
                break
            else:
                print("Invalid choice!")

        enemy_hp = enemy.stats['HP'] * (1 - damage)
        if enemy_hp <= 0:
            print("You defeated the enemy!")
            self.floor += 1
            player.level_up()
        else:
            print("The enemy is still standing!")

def main():
    player = Player()
    dungeon = Dungeon()

    while True:
        print("\n=== Menu ===")
        print("1. View Player Stats")
        print("2. Visit Shop")
        print("3. Visit Mage's Bar")
        print("4. Visit Ranger's Den")
        print("5. Clear Next Floor")
        print("6. Exit Game")
        choice = input("Choose an option: ")

        if choice == "1":
            player.display_stats()
        elif choice == "2":
            print("\nWelcome to the Shop!")
            print("1. Buy Weapon (+10% ATK) - 50 Gold")
            print("2. Exit Shop")
            shop_choice = input("Choose an option: ")
            if shop_choice == "1":
                player.buy_item("Weapon", 50)
        elif choice == "3":
            print("\nWelcome to the Mage's Bar!")
            print("1. Buy Magic Book (+10% MATK) - 50 Gold")
            print("2. Exit Mage's Bar")
            mage_choice = input("Choose an option: ")
            if mage_choice == "1":
                player.buy_item("Magic Book", 50)
        elif choice == "4":
            print("\nWelcome to the Ranger's Den!")
            print("1. Buy Arrows (+10% RAN) - 50 Gold")
            print("2. Exit Ranger's Den")
            ranger_choice = input("Choose an option: ")
            if ranger_choice == "1":
                player.buy_item("Arrows", 50)
        elif choice == "5":
            print("\nEntering the next floor...")
            dungeon.clear_floor(player)
        elif choice == "6":
            print("Exiting the game. Goodbye!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
