def count_divisors(n):
    divisors = 0
    for i in range(1, n+1):
        if n % i == 0:
            divisors += 1
    return divisors

def main():
    count = 0
    for num in range(1, 1001):  
        if count_divisors(num) == 9:
            print(f"{num} has exactly 9 divisors.")
            count += 1
    print(f"Total numbers with exactly 9 divisors: {count}")

if __name__ == "__main__":
    main()
