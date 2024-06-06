set1=set(list(map(int,input("Enter elements of set 1:").split())))
set2=set(list(map(int,input("Enter elements of set 2:").split())))
set1 &= set2
li=list(set1)
print("The intersection of two sets is:")
print(li)
