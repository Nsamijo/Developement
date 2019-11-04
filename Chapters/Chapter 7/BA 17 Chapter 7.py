#Write a program that creates this shape
#  |  1  2  3  4  5
#--+---------------
#1 |  1  2  3  4  5
#2 |  2  4  6  8 10
#3 |  3  6  9 12 15
#4 |  4  8 12 16 20
#5 |  5 10 15 20 25

size = 5

timestable = '  |'
j = 1
while j <= size:
  timestable += '  ' + str(j)
  j = j + 1
timestable = timestable + '\n'

timestable = timestable + '--+---------------\n'
i = 1
while i <= size:
  timestable = timestable + str(i) + ' |'
  j = 1
  while j <= size:
    times = i * j
    if len(str(times)) == 1:
      timestable = timestable + '  '
    else:
      timestable = timestable + ' '
    timestable = timestable + str(times)
    j = j + 1
  timestable = timestable + '\n'
  i = i + 1

print(timestable)