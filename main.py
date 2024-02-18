try:
    import random
    import time
    
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

    
    
    
    while True:
        while True:
            print("Welcome to the game!")
            print("1. Dungeon")
            print("2. Player Menu")
            print("3. Bestiary")
            print("4. Grimoire")
            print("5. Market")
            print("x. Exit")
            
            choice = input("Enter your choice: ")
            
            if choice == "1":
                print ("which Floor?")
                print ("you can go to these floors: 1-", player.highest_floor_cleared)
                floor = input("")
                try: # wierd way of making sure they dont input a letter or smth
                  floor -= 1
                  floor += 1
                  if (floor - 1) != -1 and (floor - 1) != 0:
                    enemy = Enemy(name="Goblin", level=1, health=50, attack=10, defense=0, speed=8)
                    enemy.set_stats_to_level(floor)
                    while True:
                        if enemy.health < 0:
                            print ("you won. nerd. >:(")
                            player.exp += (enemy.maxhealth / 10) + (enemy.defense) + (enemy.attack / 2) + (enemy.speed / 2) + (floor * 5)
                            if player.exp > player.exp_cap:
                                player.attack += 0.5
                                player.ranged_attack += 0.5
                                player.magic_attack += 0.5
                                player.defense += 0.2
                                player.maxhealth += 5
                                player.maxhealth *= 1.01
                                player.maxmana += 5
                                player.maxmana *= 1.01
                                player.mana = player.maxmana
                                player.health = player.maxhealth
                                player.speed += 0.25
                                player.exp = 0
                            player.highest_floor_cleared = floor
                            player.health = player.maxhealth
                            player.mana = player.maxmana
                            break
                        player.restore_mana(player.maxmana / 10)
                        if player.mana > player.maxmana:
                            player.mana = player.maxmana

                        player.heal(player.maxhealth / 100)
                        if player.health > player.maxhealth:
                            player.health = player.maxhealth

                        print ("Health:", player.health, "/", player.maxhealth)
                        print (enemy.name, "Health:", enemy.health, "/", enemy.maxhealth)
                        print ("")
                        print ("1. Melee attack")
                        print ("2. Ranged attack")
                        print ("3. Magic")
                        print ("")
                        print ("x. fuck this, this game is garbage wtf (exit)")

                        choice = input("")
                        if choice == "x":
                          break
                        if choice == "3":
                          print ("spells:")
                          for spell in player.spells:
                              print (spell)
                          print ("What spell to cast?")
                          choice = input("")
                          if choice == "Heal" or choice == "heal":
                              if player.mana > 10:
                                  player.heal(player.maxhealth / 3)
                                  player.health = round(player.health)
                                  if player.health > player.maxhealth:
                                    player.health = player.maxhealth
                                  player.mana -= 10
                              else:
                                  print ("no mana..?")
                          if choice == "Magic bolt" or choice == "magic bolt" or choice == "Magic Bolt" or choice == "magicbolt" or choice == "Magicbolt" or choice == "MagicBolt":
                              if player.mana > 10:
                                  enemy.take_damage(player.magic_attack)
                                  player.mana -= 10
                              else:
                                  print ("no mana..?")

                        if choice == "2":
                            arrows = 0
                            for items in player.items:
                                if items == "Arrow":
                                    arrows += 1
                            if arrows > 0:
                                enemy.take_damage(player.ranged_attack)
                            else:
                                print ("no arrows..?")

                        if choice == "1":
                            enemy.take_damage(player.attack)
                        
                except:
                    print ("stupid monkey.!!..!!!")
                
            elif choice == "2":
                print ("1. Player Stats")
                choice = input("")
                if choice == "1":
                    print_player_stats(player)
                    
                
            elif choice == "3":
                pass

            elif choice == "4":
                pass

            elif choice == "5":
                pass
                
            elif choice == "x":
                print ("no. press the X, lazy.")
                time.sleep(99999)
            else:
                print("Stupid monkey select a number between 1-4.")

except Exception as e:
    print (e)
