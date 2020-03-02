shipX = 5
shipY = 4
missileX = 0
missileY = 0
while missileX != shipX or missileY != shipY:
  if missileX < shipX:
    missileX = missileX + 1
  elif missileX < shipX:
    missileX = missileX - 1
  if missileY > shipY:
    missileY = missileY - 1
  elif missileY < shipY:
    missileY = missileY + 1
print()