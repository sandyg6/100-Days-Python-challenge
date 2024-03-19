number=int(input("Enter the number: "))
count=0
rem=0
Number=number
while number!=0:
    number//=10
    count+=1
for i in range(0, count):
    N=Number%10
    rem=rem*10+N
    Number//=10
print("The reversed number is :", rem)
