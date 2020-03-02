floorDiv = lambda x: lambda y: x // y
a = 13
b = 3

f = floorDiv(a)
ans1 = f(b)

ans2 = floorDiv(a)(b)

print()