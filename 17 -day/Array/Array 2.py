print()
print("Two dimensitional array:")
mat = [
    [10,20,30],
    [40,50,60],
    [70,80,90]
]
print(mat)
print()
#printing row
print("Row of the matrix by using for loops:")
for i in mat:
    print(i)
print()
#printing specific elements
print()
print("print specific elements of the matrix:")
print(mat[0][1])
print(mat[1][1])
print(mat[2][1])
print(mat[0][2])

print()
print("print specific elements of the matrix by using for loops:")
for i in range(len(mat)):
    for j in range(len(mat[i])):
        print(mat[i][j])

#Both result are same .
# print()
# for i in (mat):
#     for j in i :
#         print(j)















