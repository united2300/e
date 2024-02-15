try:
  # World game thing


  import random
  import time
  
  from VarAndDefs import *
  
  Dungeon = Dungeon(level=1)
  input("")
  e = Dungeon.spawn_enemy()
  input("")
  p.hp -= Calculate_damage("Atk", p, e)
  input("")
  print ("hi")
  input("")
except Exception as error:
  print (error)
  input("")
