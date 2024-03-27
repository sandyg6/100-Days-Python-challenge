n=int(input("Enter a number:"))
num=n
number=n
numb=[]
count = 0
while n!=0:
    r=n%10
    n//=10
    count+=1
for i in range(0,count):
    rem=num%10
    s=rem**count
    num//=10
    numb.append(s)
ams=sum(numb)
if number==ams:
    print("The given number is an armstrong number.")
else:
    print("The given number is not an armstrong number.")
