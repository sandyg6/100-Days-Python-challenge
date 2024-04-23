def solid_rectangle(rows, cols):
    for i in range(rows):
        for j in range(cols):
            print("*", end=" ")
        print()

def hollow_rectangle(rows, cols):
    for i in range(rows):
        for j in range(cols):
            if i == 0 or i == rows - 1 or j == 0 or j == cols - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

def main():
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))

    print("\nSolid Rectangle Star Pattern:")
    solid_rectangle(rows, cols)

    print("\nHollow Rectangle Star Pattern:")
    hollow_rectangle(rows, cols)

if __name__ == "__main__":
    main()
