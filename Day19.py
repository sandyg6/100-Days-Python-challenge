base=int(input("Enter the base number:"))
power=int(input("Enter an exponent number:"))
tot=1
for i in range(0,power,1):
    tot=base*tot
print(f"The value of {base}^{power} is",tot)
