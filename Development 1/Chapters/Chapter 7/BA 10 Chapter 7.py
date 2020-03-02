# Pyramid with spaces at the end
height = 3
s = ''
i = 0
while i < height:
  j = 0
  while j < height - i - 1:
    s = s + ' '
    j = j + 1
  while j < height + i:
    s = s +'*'
    j = j + 1
  while j < height + 2:
    s = s +' '
    j = j + 1
  s = s + '\n'
  i = i + 1
print()