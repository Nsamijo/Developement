# This program draws  the following shape:
# +++++++++
# +       +
# +*      +
# +**     +
# +***    +
# +****   +
# +*****  +
# +****** +
# +++++++++

s = ''
size = 9
row = 0

while row < size:
  col = 0
  if row == 0 or row == 8:
    while col < size:
      s += '+'
      col += 1
  else:
    while col < size:
      if col == 0 or col == 8:
        s += '+'
      elif col < row:
        s += '*'
      else:
        s += ' '
      col += 1
  s += '\n'
  row += 1

print()