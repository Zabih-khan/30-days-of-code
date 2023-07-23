# for row in range(7):
#     for col in range(7):
#         if (((row == col or col == 3) or row == 3)  or col == 7 - 1 - row):
#             print('*', end=' ')
#         else:
#             print('.',end= ' ')
#     print()

for row in range(7):
    for col in range(7):
        if row == col:
            print("*", end=' ')
        elif row + col == 6:
            print("*", end=' ')
        elif col == 3:
            print('*', end=' ')
        elif  row == 3:
            print('*', end=' ')
        else:
            print('.',end=' ')
    print()