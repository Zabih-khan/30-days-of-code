#This program only print duplicate element.
arr = [2,2,3,4,5,3,4,]
arr_set = set()
for i in arr:
    if i in arr_set:
        print(i,end=" ")
    else:
        arr_set.add(i)
