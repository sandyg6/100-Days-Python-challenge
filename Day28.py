n=int(input("Enter a integer:"))
r=0
number=n
num=str(n)
for i in range(0,len(num)):
    r=10*r+n%10
    n//=10
if number==r:
    print("The given number is palindrome.")
else:
    print("The given number is not a palindrome.")