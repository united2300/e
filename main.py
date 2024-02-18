import random

class Player:
    def __init__(self, name, level, exp, exp_cap, health, mana, defense, speed, attack, ranged_attack, magic_attack, highest_floor_cleared):
        self.name = name
        self.level = level
        self.exp = exp
        self.exp_cap = exp_cap
        self.health = health
        self.maxhealth = health
        self.mana = mana
        self.maxmana = mana
        self.defense = defense
        self.speed = speed
        self.attack = attack
        self.ranged_attack = ranged_attack
        self.magic_attack = magic_attack
        self.highest_floor_cleared = highest_floor_cleared

    def take_damage(self, damage):
        self.health -= damage

    def heal(self, amount):
        self.health += amount

    def use_mana(self, amount):
        self.mana -= amount

    def restore_mana(self, amount):
        self.mana += amount

# Initialize the class
player = Player(name=input("Give me a name you stupid 3D monkey. --> "), level=1, exp=0, exp_cap=100, health=100, mana=100, defense=0, speed=1, attack=10, ranged_attack=12.5, magic_attack=10, highest_floor_cleared=0)

class Enemy:
    def __init__(self, name, level, health, attack, defense, speed):
        self.name = name
        self.level = level
        self.health = health
        self.maxhealth = health
        self.attack = attack
        self.defense = defense
        self.speed = speed

    def set_stats_to_level(self, floor):
        self.level = self.level + (1 - floor)
        self.health = self.health + (1 * (floor - 1))
        self.maxhealth = self.health
        self.attack = self.attack + (0.2 * (floor - 1))
        self.defense = self.defense + (0.2 * (floor - 1))
        self.speed = self.speed + (0.1 * (floor - 1))

    def take_damage(self, damage):
        self.health -= damage

    def attack_player(self, player):
        player.take_damage(self.attack)

# Example initialization of an enemy
enemy = Enemy(name="Goblin", level=1, health=50, attack=10, defense=5, speed=8)



while True:
    while True:
        
