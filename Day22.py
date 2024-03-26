A,B=map(int,input("Enter two integers:").split())
a=A
b=B
while b!=0:
    r=a%b
    a=b
    b=r
print(f"The GCD of {A} and {B} is",a)
