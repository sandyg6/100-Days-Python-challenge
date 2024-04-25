def print_diamond_pattern(rows):
    # Upper part of the diamond
    for i in range(1, rows + 1):
        # Print leading spaces
        for j in range(1, rows - i + 1):
            print(" ", end="")
        # Print numbers in increasing order
        for j in range(1, 2 * i):
            print(j, end="")
        print()

    # Lower part of the diamond
    for i in range(rows - 1, 0, -1):
        # Print leading spaces
        for j in range(1, rows - i + 1):
            print(" ", end="")
        # Print numbers in increasing order
        for j in range(1, 2 * i):
            print(j, end="")
        print()

# Number of rows in the diamond
rows = 5
print_diamond_pattern(rows)
