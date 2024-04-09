def maxHandshake(n):
    return int((n * (n - 1)) / 2)

n = int(input("Enter a value:"))
print(maxHandshake(n))
