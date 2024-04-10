def quadrants(x, y):
    x = int(x)
    y = int(y)
    if (x>0 and y>0):
        print("1st Quadrant")
    elif (x<0 and y>0):
        print("2nd Quadrant")
    elif (x<0 and y<0):
        print("3rd Quadrant")
    elif (x>0 and y<0):
        print("4th Quadrant")
    elif (x==0 and y==0):
        print("origin")

a, b = input("Enter x, y coordinates: ").split()
quadrants(a, b)
