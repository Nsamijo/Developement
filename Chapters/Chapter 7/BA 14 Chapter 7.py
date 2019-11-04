l = 4
s = ''
i = 0
while i < l / 2:
  j = 0
  while j < l / 2:
    s = s + '*'
    j = j + 1
  while j < l:
    s =  s + '+'
    j = j + 1
  i = i + 1
  s = s + '\n'
i = 0
while i < l / 2:
  j = 0
  while j < l / 2:
    s = s + '-'
    j = j + 1
  while j < l:
    s = s + '='
    j = j + 1
  i = i + 1
  s = s + '\n'
print()