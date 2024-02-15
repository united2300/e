try:
    import random
    import time
    
    # Variables
    
    
    # Player
    
    p_hp = 100
    p_atk = 1
    p_ratk = 1
    p_matk = 1
    p_mana = 100
    p_def = 0
    p_spd = 0
    
    spells = {
        'Magic bolt': {
            'description': 'Creates a magic bolt and launches it at your enemy.',
            'mana_cost': 10,
            'damage': 10
        },
        'Lightning Bolt': {
            'description': 'Strikes with lightning',
            'mana_cost': 10,
            'damage': 10
        },
        'Heal': {
            'description': 'Restores health',
            'mana_cost': 10,
            'healing': 40
        }
    }
    
    
    class Player:
        def __init__(self, hp, atk, ratk, matk, mana, defense, spd):
            self.level = 1
            self.exp = 0
            self.expcap = 100
            self.hp = hp
            self.maxhp = hp
            self.atk = atk
            self.matk = matk
            self.ratk = ratk
            self.mana = mana
            self.maxmana = mana
            self.defense = defense
            self.spd = spd
    
    
    
    # Example instantiation
    p = Player(p_hp, p_atk, p_ratk, p_matk, p_mana, p_def, p_spd)
    
    
    
    
    
    # Enemy
    
    class Enemy:
        def __init__(self, lvl, name, exp_reward, hp, atk, ratk, matk, mana, defense, spd):
            self.level = lvl
            self.name = name
            self.exp_reward = exp_reward
            self.hp = hp
            self.maxhp = hp
            self.atk = atk
            self.matk = matk
            self.ratk = ratk
            self.mana = mana
            self.maxmana = mana
            self.defense = defense
            self.spd = spd
    
    
    # Create enemy instances and store them in a dictionary
    enemy_dict = {
        'Goblin': Enemy(lvl=1, name="Goblin", exp_reward=10, hp=10, atk=3, ratk=0, matk=0, mana=0, defense=0, spd=1),
        'Skeleton': Enemy(lvl=1, name="Skeleton", exp_reward=20, hp=20, atk=5, ratk=0, matk=0, mana=0, defense=1, spd=2),
        'Orc': Enemy(lvl=1, name="Orc", exp_reward=30, hp=30, atk=10, ratk=0, matk=0, mana=0, defense=2, spd=3),
        # Add more enemies as needed
    }
    
    
    
    class Dungeon:
        def __init__(self, level):
            self.level = level
            self.spawning = False
            
        def spawn_enemy(self):
            if self.spawning == False:
              self.spawning == True
            else:
            
                # Randomly select an enemy from the enemy dictionary
                enemy_name = random.choice(list(enemy_dict.keys()))
        
                # set the enemy
                e = enemy_dict[enemy_name]
                
                e.level += self.level
                e.exp_reward += self.level
                e.hp += (self.level * 2)
                e.atk += (self.level / 5)
                e.ratk += (self.level / 5)
                e.matk += (self.level / 5)
                e.mana += (self.level * 2)
                e.defense += (self.level / 5)
                e.spd += (self.level / 2)
                
                # Generate a random factor between 85 and 115 (equivalent to 0.85 and 1.15)
                random_factor = random.randint(85, 115) / 100
                
                # Apply the random factor to the enemy's attributes
                e.hp = round(e.hp * random_factor, 2)
                e.atk = round(e.atk * random_factor, 2)
                e.matk = round(e.matk * random_factor, 2)
                e.ratk = round(e.ratk * random_factor, 2)
                e.mana = round(e.mana * random_factor, 2)
                e.defense = round(e.defense * random_factor, 2)
                e.spd = round(e.spd * random_factor, 2)
                
                print(f"You tracked down a level {e.level} {e.name}!")
                return e
    
    
    
    
    
    
    # Logic-neccesary
    
    def Calculate_damage(type, a, t):
    
      if type == "SHeal": # Self Heal
        a.hp += a.matk
      if type == "GHeal": # Group Heal
        for target in t:
          target.hp += a.matk
      
      # Calculate normal attack damage.
      if type == "Atk":
        if t.defense < a.atk:
          t.hp -= (a.atk - t.defense)
        else:
          if t.hp / 100 < 1:
            t.hp -= (t.hp / 100)
          else:
            t.hp -= 1
    
      # Calculate magic attack damage
      elif type == "Matk":
        if a.matk > (t.matk * 2):
          t.hp -= a.matk
        elif a.matk > t.matk:
          t.hp -= a.matk - t.matk
        else:
          # heal by 1/10th of attacker matk if attacker magic attack < target magic attack
          t.hp += ((t.matk - a.matk) / 10)
    
      # Calculate ranged attack damage
      elif type == "Ratk":
        if a.ratk > t.spd:
          t.hp -= a.ratk
        elif a.ratk > (t.spd / 2):
          t.hp -= (a.ratk / 1.5)
        elif a.ratk > (t.spd / 2.5):
          t.hp -= (a.ratk / 2)
        elif a.ratk > (t.spd / 3.33):
          t.hp -= (a.ratk / 3)
        elif a.ratk > (t.spd / 4):
          t.hp -= (a.ratk / 6)
        elif a.ratk > (t.spd / 6):
          t.hp -= (a.ratk / 12)

      return t.hp
except Exception as error:
    print(error)
    input("")
