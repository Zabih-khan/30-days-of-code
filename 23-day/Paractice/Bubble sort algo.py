a = [3,4,2,1,6]
for i in range(len(a)):
    for j in range(0,len(a)-i-1):
        if a[j] > a[j+1]:
            t = a[j]
            a[j] = a[j+1]
            a[j+1] = t
print("Sorted list is;")
print(a)