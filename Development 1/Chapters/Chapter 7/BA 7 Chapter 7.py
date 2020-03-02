h = 5
s = ''
i = 0
while i < h:
  j = 0
  while j < h - i - 1:
    s = s + ' '
    j = j + 1
  while j < h:
    s = s + '*'
    j = j + 1
  i = i + 1
  s = s + '\n'
print(s)