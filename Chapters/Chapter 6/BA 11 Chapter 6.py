base = 5
fig = ''
i = 1

while i < base:
    j = 1
    while j <= base - i:
        fig = fig + str(base - j)
        j = j + 1
    i = i + 1
    fig = fig + '\n'

print(fig)