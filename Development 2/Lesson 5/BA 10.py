def lineHoles(i, n, sym, times):
  if i == n:
    return ''
  else:
    rest = lineHoles(i + 1, n, sym, times)
    if i % times == 0:
      return str(i) + rest
    else:
      return sym + rest

n = 7
sym = '+'
multipleOf = 3
s = lineHoles(0, n, sym, multipleOf)
print(s)