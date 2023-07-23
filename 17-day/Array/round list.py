nums = [22.4,4.5,5.0,2.1]

print("original list:", nums)
print("Result")
length = len(nums)
print(sum(list(map(round,nums)) * length))
print()
print(list(map(round,nums)))