try:
  # World game thing
  
  from VarAndDefs import *
  
  Dungeon = Dungeon(1)
  e = Dungeon.spawn_enemy()
  Calculate_damage("Atk", p, e)
  print ("hi")
  input("")
except Exception as error:
  print (error)
  input("")
