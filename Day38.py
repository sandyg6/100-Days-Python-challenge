arr = ['zero','one','two','three','four','five','six','seven','eight','nine']
 
def number_2_word(n):
    if(n==0):
        return ""
     
    else:
        small_ans = arr[n%10]
 
        ans = number_2_word(int(n/10)) + small_ans + " "
     
    return ans
 
n = int(input())
print("Number Entered was : ", n)
print("Converted to word it becomes: ",end="")
print(number_2_word(n))
