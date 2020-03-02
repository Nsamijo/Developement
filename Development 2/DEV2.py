def func1(x, y):
  return x + y

def func2(x):
  return func1(x, x)

def func3(x, y, z):
  return func1(x, y) * z

a = func1(5, 2)
b = func2(4)
c = func3(2, 3, 4)
print()