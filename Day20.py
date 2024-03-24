number=int(input("Enter a number:"))
lst=[]
for i in range(1,number+1):
    rem=number%i
    if rem==0:
        lst.append(i)
    else:
        pass
print(f"The factors of {number} are",",".join(map(str,lst)))
