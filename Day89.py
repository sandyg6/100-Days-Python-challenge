li = list(map(int, input("Enter the elements of the list:").split()))
li = [x for x in li if x%5!=0 and x%7!=0]
print(li)
