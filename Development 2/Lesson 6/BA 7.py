def fun(n, f):
    s = ''
    m = 1
    while m <= n :
       s = s + f(m)
       m = m + 1
    return s

a = 10
line = fun(a, lambda x : '*')
timeTableThree = fun(a, lambda x: str(x * 3) + '-')

print()

surround = lambda x :  '<'  + str(x) + '>'
surroundIfOdd = lambda x: surround(x) if x % 2 != 0 else str(x)
b = 8
numbers = fun(b, surround)
numbersOdd = fun(b, surroundIfOdd)

print()