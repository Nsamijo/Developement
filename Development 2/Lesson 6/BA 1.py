def mul(a):
  l = lambda b: a * b
  return l

x = 3
f = mul(x)
v1 = f(x)
v2 = mul(x)(x)

x = 2
g = mul(x)
w1 = g(v2)
w2 = mul(x)(v1)
print()