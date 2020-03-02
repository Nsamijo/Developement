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

def OR(p, q):
  return lambda a, b : p(a, b) or q(a, b)

top = lambda x, y : x == 0
left = lambda x, y : y == 0
s1 = drawFig(3, 3, top)
s2 = drawFig(3, 3, left)
fig = OR(top, left)
s = drawFig(5, 5, fig)
print()