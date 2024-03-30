leap= int(input("Enter a year:"))
if leap%400==0:
    print(f"{leap} is a leap year")
elif leap%100==0:
    print(f"{leap} is not a leap year")
elif leap%4==0:
    print(f"{leap} is a leap year")
else:
    print(f"{leap} is not a leap year")
