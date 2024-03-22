number=int(input("Enter a number:"))
tot=0
for i in range(1,number):
    if number%i==0:
        tot=tot+i
if tot==number:
    print("The number is Perfect number.")
else:
    print("The number is not a Perfect number.")
