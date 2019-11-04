# Diamond

l = 5
s = ''
i = 0

while i < l / 2:
  j = 0
  while j < l / 2 - i - 1:
    s = s + ' '
    j = j + 1
  while j < l / 2 + i:
    s = s + '*'
    j = j + 1
  while j < l:
    s = s + ' '
    j = j + 1
  s = s + '\n'
  i = i + 1
i = 1
while i < l / 2:
  j = 0
  while j < i:
    s = s + ' '
    j = j + 1
  while j < l - i:
    s = s + '*'
    j = j + 1
  while j < l:
    s = s + ' '
    j = j + 1
  s = s + '\n'
  i = i + 1
print(s)