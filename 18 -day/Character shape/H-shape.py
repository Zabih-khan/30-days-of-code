for row in range(7):
    for col in range(7):
        if col == 0:
            print("*",end=" ")
        elif col == 6:
            print("*",end="")
        elif col == 2 and row == 3:
            print("*",end=" ")
        elif col == 3 and row == 3:
            print("*", end=" ")
        elif col == 4 and row == 3:
            print("*",end=" ")
        else:
            print(end="  ")
    print()