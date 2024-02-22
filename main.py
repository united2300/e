try:
    import random
    import time

    menu = "main"
    
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
            self.weapons = []
            self.items = []
            self.spells = ["Heal", "Magic bolt"]
    
    # Initialize the class
    player1 = Player(name=input("Give me a name you stupid 3D monkey. --> "), level=1, exp=0, exp_cap=100, health=100, mana=100, defense=0, speed=1, attack=10, ranged_attack=12.5, magic_attack=10, highest_floor_cleared=1)
    
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
    
    # Example initialization of an enemy
    enemy = Enemy(name="Goblin", level=1, health=50, attack=10, defense=5, speed=8)
    
    


    def print_player_stats(player):
        print("Player Stats:")
        print(f"Name: {player.name}")
        print(f"Level: {player.level}")
        print(f"Experience: {player.exp}/{player.exp_cap}")
        print(f"Health: {player.health}/{player.maxhealth}")
        print(f"Mana: {player.mana}/{player.maxmana}")
        print(f"Defense: {player.defense}")
        print(f"Speed: {player.speed}")
        print(f"Attack: {player.attack}")
        print(f"Ranged Attack: {player.ranged_attack}")
        print(f"Magic Attack: {player.magic_attack}")
        print(f"Highest Floor Cleared: {player.highest_floor_cleared}")


    def print_menus(menu):
        if menu == "main":
            print ("1. Dungeon")
            print ("2. City")
            print ("3. Player stats")
        elif menu == "city":
            print ("1. aDvEnTuReRs gUiLd")
            print ("2. Smithy")
            print ("3. Rangers Nest")
            print ("4. Mages Den")
        elif menu == "player_stats":
            print_player_stats(player1)
    
    while True:
        try: # Error Handling...
            
            while True:
                
                if menu == "main":
                    print_menus(menu)
                    print ("")
                    choice = input("--> ")

                if menu == "city":
                    print_menus(menu)
                    print ("")
                    choice = input("--> ")

                if menu == "player_stats":
                    print_menus(menu)
                    print ("")
                    choice = input("--> ")
                
        except Exception as e:
            print (e)
            input("Press Enter to Exit")
        
    


except Exception as e:
    print (e)
    input("Press Enter to Exit")

print ("")
input("Game Closing... Press Enter to Exit")
