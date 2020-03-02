# Upside down pyramid with spaces at the end
height = 5
s = ''
i = 0
while i < height:
  j = 0
  while j < i:
    s = s + '-'
    j = j + 1
  while j < height + 4 - i:
    s = s +'*'
    j = j + 1
  while j < height + 4:
    s = s + '-'
    j = j + 1
  s = s + '\n'
  i = i + 1
print()