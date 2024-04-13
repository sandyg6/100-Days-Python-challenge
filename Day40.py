import math

n = int(input('Enter the number of people :'))

r = int(input('Enter the number of seats :'))

num = math.factorial(n)

den = math.factorial(n-r)

ways = num//den

print(str(ways))
