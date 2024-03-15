def area(l,b):
    return (0.5)*l*b
length, breadth = map(int,input().split())
print("The area of rectangle is ",int(area(length,breadth)))
