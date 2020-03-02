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

def AND(p, q):
  return lambda c, d : p(c, d) and q(c, d)

n = 5
tri1 = lambda x, y : x <= y
tri2 = lambda x, y : (n - 1 - x) <= y
sa = drawFig(n, n, tri1)
sb = drawFig(n, n, tri2)
fig1 = OR(tri1, tri2)
fig2 = AND(tri1, tri2)
s1 = drawFig(n, n, fig1)
s2 = drawFig(n, n, fig2)
print()