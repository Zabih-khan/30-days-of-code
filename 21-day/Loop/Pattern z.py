result = ""
for row in range(0,7):
    for colume in range(0,7):
        if ((row == 0 or row == 6) and colume >= 0 and colume <= 6 ) or row + colume == 6:
            result = result + "!"
        else:
            result = result + " "
    result = result + "\n"
print(result)
print("~~~~~~~~~~~~~")
print()

# This code for M.
result = ""
for row in range(0,7):
    for colume in range(0,7):
        if ((colume == 0 or colume == 6) or (row == 1 and (colume == 2 or colume == 4)) or (row == 2 and colume ==3)) :
            result = result + "* "
        else:
            result = result + "  "
    result = result + "\n"
print(result)