def then (f,g):
  return lambda x : g(f(x))
incr = lambda x: x + 1
incr2 = lambda y: y + 2
mul2 = lambda z: z* 2
pow2 = lambda w: w * w
a = 5
b = 3
c = incr(a)
d = incr2(b)
incrpow = then(incr, pow2)
a = incrpow(a)
powmul = then(pow2, mul2)
e = powmul(d)
print()