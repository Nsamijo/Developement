base = 5
fig = ''
i = 1

while i <= base:
  j = 1
  while j <= i:
    fig = fig + str(j)
    j = j + 1
  fig = fig + '\n'
  i = i + 1

print()