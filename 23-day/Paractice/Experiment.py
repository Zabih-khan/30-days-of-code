n = int(input("Enter odd number"))
#Validate number is odd or not
if n%2 == 0:
    print(f"invalid input {n}, please enter odd number")
    exit(1)
#Find mid
mid = n//2
i = 0
while i < n:
    j = 0
    while j<n:
        #Put * at mid row and colume.
        if i == mid or j == mid:
            print("*",end="")
        #Diagonal i == j
        elif i == j:
            print("*",end="")
        elif i + j == n-1:
            print("*",end="")
        else:
            print(".",end="")
        j = j + 1
    i = i + 1
    print()
