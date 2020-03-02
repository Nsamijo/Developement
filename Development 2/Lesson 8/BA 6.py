def drawFig(width, height, fig):
  s = ''
  row = 0
  while row < height:
    column = 0
    while column < width:
      if fig(row,column):
        s = s + '*'
      else:
        s = s + ' '
      column = column + 1
    s = s + '\n'
    row = row + 1
  return s

def AND(p, q):
  return lambda a, b : p(a, b) and q(a, b)

def flipHorizontal(p, w):
  return lambda c, d : p(w - (c + 1), d)

leftTri = lambda x, y : x <= y
rightTri = flipHorizontal(leftTri, 5)
fig = AND(leftTri, rightTri)
s = drawFig(5, 5, fig)
print()