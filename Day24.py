def max(a,b):
    if a>b:
        print("Greatest number is",a)
    elif a==b:
        print("Both are equal")
    else:
        print("Greatest number is",b)
number1, number2=map(int,input("Enter two integers:").split())
max(number1,number2)
