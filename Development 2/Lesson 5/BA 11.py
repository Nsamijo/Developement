def repeat(n, sym):
  print()
  if n == 0:
    return ''
  else:
    return sym + repeat(n - 1, sym)


def line(n):
  return repeat(n, '*')

def rectangle(rows, cols):
  l = line(cols)
  rect = repeat(rows, l + '\n')
  return rect

r = 4
c = 5
rec = rectangle(r, c)
print()