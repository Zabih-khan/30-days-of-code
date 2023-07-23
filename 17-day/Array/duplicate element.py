arr = list(map(int,input("input all the number in single line:").strip().split()))
num_set =set()
for i in range(len(arr)):
    if arr[i] in num_set:
        print(arr[i])
    else:
        num_set.add(arr[i])


