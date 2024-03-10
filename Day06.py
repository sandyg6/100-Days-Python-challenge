n=int(input("Enter the number of terms:"))
a,b=0,1
lst=[0,1]
for i in range(2,n):
    c=a+b
    a=b
    b=c
    lst.append(c)
print("Fibonancci series:" , ",".join(map(str,lst)))
