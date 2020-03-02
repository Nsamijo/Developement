mul = lambda a: lambda b: a * b

mul1 = mul(1)
mul2 = mul(2)
mul3 = mul(3)

ans = mul2(mul1(2)) * mul3(2)
ans1 = mul1(mul2(mul3(1)))
ans2 = mul(1)(mul(2)(mul(3)(1)))

print()