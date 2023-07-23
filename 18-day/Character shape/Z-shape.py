for row in range(6):
    for col in range(6):
        if row == 0 or row == 5:
            print("*", end=" ")
        elif row + col == 5:
            print("*",end=" ")
        else:
            print(end="  ")
    print()


