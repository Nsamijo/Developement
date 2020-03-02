def drawFig(width, height, fig):
  s = ''
  row = 0
  while row < height:
    column = 0
    while column < width:
      if fig(row, column):
        s = s + '*'
      else:
        s = s + ' '
      column = column + 1
    s = s + '\n'
    row = row + 1
  return s

n = 5
s = drawFig(n, n, lambda x, y : x + y < 5)
print()