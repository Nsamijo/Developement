h = 5
i = 0
s = ''
while i < h - 2:
  j = 0
  while j <= i:
    s = s + '*'
    j = j + 1
  i = i + 1
  s = s + '\n'
while i < h:
  j = 0
  while j < h - i:
    s = s + '*'
    j = j + 1
  i = i + 1
  s = s + '\n'
print(s)