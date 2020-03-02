x = 2
divisibleBy = ''

while x <= 10:
  divisor = 2
  while divisor < 5:
    if x % divisor == 0:
      divisibleBy = str(x) + ' is divisible by ' + str(divisor)
    else:
      divisibleBy = str(x) + ' is NOT divisible by ' + str(divisor)
    divisor = divisor + 1
  x = x + 1

print()