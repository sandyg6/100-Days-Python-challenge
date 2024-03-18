start=int(input("Enter the starting range:"))
end=int(input("Enter the ending range:"))
for i in range(start,end+1):
    total=(end*(end+1))//2 - ((start-1)*(start))//2
print("The sum of the given range is:",total)
