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
        self.expcap = 10
        self.hp = hp
        self.maxhp = hp
        self.atk = atk
        self.matk = matk
        self.ratk = ratk
        self.mana = mana
        self.maxmana = mana
        self.def = defense
        self.spd = spd




# Example instantiation
p = Player(p_hp, p_atk, p_ratk, p_matk, p_mana, p_def, p_spd)




# Logic-neccesary

def Calculate_damage(type, a, t):
  global type, a, t # a = attacker, t = target

  if type == "SHeal": # Self Heal
    a.hp += a.matk
  if type == "GHeal": # Group Heal
    for target in t:
      target.hp += a.matk
  
  # Calculate normal attack damage.
  if type == "Atk":
    if t.def < a.atk:
      t.hp -= (a.atk - t.def)
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
