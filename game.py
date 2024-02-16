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

class Dungeon:
    def __init__(self):
        self.floor = 1
        self.enemy_level = 1

    def generate_enemy(self):
        # Simulate enemy generation based on floor and player's level
        self.enemy_level = max(1, self.floor // 10)  # Enemies get stronger every 10 floors
        enemy_power = self.enemy_level * random.uniform(0.8, 1.2)  # Randomness in enemy power
        return enemy_power

    def clear_floor(self, player):
        enemy_power = self.generate_enemy()
        if player.power > enemy_power:
            print("Floor cleared!")
            self.floor += 1
            player.level_up()
            return True
        else:
            print("You were defeated by the enemy.")
            return False

def main():
    player = Player()
    dungeon = Dungeon()

    while True:
        print("\n=== Current Status ===")
        player.display_stats()
        print("======================")

        input("Press Enter to clear the next floor...")

        if not dungeon.clear_floor(player):
            print("Game Over!")
            break

if __name__ == "__main__":
    main()
