def fold(f, acc, current, threshold):
  print()
  if current > threshold:
    return acc
  else:
    return fold(f, f(acc, current), current + 1, threshold)

n = 10
f1 = lambda x, y: x + y
f2 = lambda x, y: x - y
res = fold(f1, 0, 1, n)
print()