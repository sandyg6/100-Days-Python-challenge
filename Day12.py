number=int(input("Enter a number:"))
sum=0
while number!=0:
    num=number%10
    sum=sum+num
    number//=10
print("The sum of digits of the number is ",sum)
    
