isEven = lambda x : x % 2 == 0
def then(f, g):
  return lambda x : g(f(x))
incr = lambda x : x + 1
increven = then(incr, then(incr, isEven))
a = 6
res = increven(a)
incrDecrEven = then(incr, then(lambda x: x - 1,isEven))
res2 = incrDecrEven(a)
print()