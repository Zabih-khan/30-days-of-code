for row in range(7):
    for col in range(7):
        if col == 0:
            print("*", end=" ")
        elif col == 6:
            print("*",end=" ")
        elif (col == row) :
            print("*",end =" ")
        else:
            print(end ="  ")
    print()
