n=int(input("Enter a number:"))
fact=[]
for i in range(1,n+1):
    rem=n%i
    if rem==0:
        fact.append(i)
    else:
        pass
if n==1:
    print("The number is a composite number.")
elif fact[0]==1 and fact[1]==n:
    print("The number is a prime number.")
else:
    print("The number is not a prime number.")
