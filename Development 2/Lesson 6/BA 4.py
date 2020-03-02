asterisk = lambda s: s + '*'
plus = lambda s: s + '+'
one = lambda s: s + '1'
space = lambda s: s + ' '
empty = lambda s: s
def then (f,g):
  return lambda x:g(f(x))

s1 = then(asterisk, then(plus, then(space, asterisk)))
a = s1('')
b = s1('b: ')

s2 = then(one,then(space, one))
c = s2('')
d = s2('d: ')

s3 = then(plus, then(space, then(plus, empty)))
e = s3('')
f = s3('f: ')
print()