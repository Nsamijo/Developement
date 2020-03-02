OR = lambda f, g: lambda x: f(x) or g(x)

AND = lambda f, g: lambda x: f(x) and g(x)

def CONCAT(f, g): 
  return lambda x: str(f(x)) + str(g(x))

f1 = lambda x: x % 2 != 0
f2 = lambda x: x > 0
surround = lambda x: '[' + str(x) + ']'
toStar = lambda x: '*'

a = -7
b = 9
c = 5
res1 = OR(f1, f2)(a)
res1b = AND(f1, f2)(a)
res2 = OR(f1, f2)(b)
res2b = AND(f1, f2)(b)
res3 = CONCAT(surround, toStar)(c)
res4 = CONCAT(toStar, surround)(c)
print()