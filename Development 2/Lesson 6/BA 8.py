difference = lambda x, y: lambda z:x(z) - y(z)

half = lambda x: x / 2
squared = lambda x: x ** 2
f1 = half
f2 = squared
f = difference(f1, f2)
x = 10
ans = f(x)
print()