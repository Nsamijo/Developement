def drawFig(width, height, fig):
  s = ''
  row = 0
  while row < height:
    column = 0
    while column < width:
      if fig(row, column):
        s = s + '*'
      else:
        s = s + 'X'
      column = column + 1
    s = s + '\n'
    row = row + 1
  return s

fig = lambda x, y :(x % 2 == 0) == (y % 2 == 0) 
s = drawFig(5, 5, fig)
print()