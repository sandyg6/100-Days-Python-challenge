n=int(input("Enter a number: "))
N=n
Number=n
count=0
lst=[]
while n!=0:
    n//=10
    count+=1

def fact(n):  
    return 1 if (n==1 or n==0) else n * fact(n - 1);  
    
for i in range(0,count):
    rem=N%10
    N//=10
    factorial=fact(rem)
    lst.append(factorial)
total=sum(lst)

if total==Number:
    print("The given number is a strong number")
else:
    print("The given number is not a strong number")
