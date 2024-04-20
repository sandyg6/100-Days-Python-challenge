def count_digit_3(n):
    count = 0
    for i in range(n+1):
        count += str(i).count('3')
    return count

n=int(input())
result = count_digit_3(n)
print(f"Number of times digit 3 occurs from 0 to {n}: {result}")
