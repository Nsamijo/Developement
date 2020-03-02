id = lambda x : x
square = lambda x : x ** 2
incrOne = lambda x : x + 1

def then(f, g):
  return lambda x : g(f(x))

def repeat(f, n):
  if n == 0:
    return id
  else:
    return then(f, repeat(f, n - 1))



a = 2
b = 5
repSquare = repeat(square, a)
repIncr = repeat(incrOne, b)
x = 4
y = repSquare(x)
z = repIncr(x)
print()