def generate_pascal_triangle(rows):
    triangle = []
    for i in range(rows):
        if i == 0:
            triangle.append([1])
        else:
            row = [1]
            for j in range(1, i):
                row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
            row.append(1)
            triangle.append(row)
    return triangle

def print_pascal_triangle(triangle):
    for row in triangle:
        print(" ".join(map(str, row)).center(len(triangle[-1]) * 2))

rows = int(input("Enter the number of rows for Pascal's triangle: "))
triangle = generate_pascal_triangle(rows)
print_pascal_triangle(triangle)
