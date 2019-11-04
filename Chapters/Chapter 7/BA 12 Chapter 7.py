side = 5
s = ''
i = 0
while i < side:
  s += '*'
  i += 1
s += '\n'
i = 0
while i < 3:
  j = 0
  while j < 3:
    s += ' '
    j += 1
  s += '\n'
  i += 1
i = 0
while i < side:
  s += '*'
  i += 1
s += '\n'
print(s)