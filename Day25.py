def max(a,b,c):
    if a>b:
        if a>c:
            print("Greatest number is",a)
    elif a<b:
        if b<c:
            print("Greatest number is",c)
        else:
            print("Greatest number is",b)
    else:
        if a==b and b==c and c==a:
            print("All numbers are equal")
            
n1,n2,n3=map(int,input("Enter three integers:").split())
max(n1,n2,n3)
