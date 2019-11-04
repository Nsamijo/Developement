x = 0
while x < 12:
    x = x + 1
    if x % 2 == 0:
        s = str(x) + ' is even'
    elif x == 5:
        s = '*** ' + str(x) + ' is odd ***'
    else:
        s = str(x) + ' is odd'
print()