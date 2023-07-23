lst = [1,2,3,4,(2,4),5,5,6,7]
# count = 0
# for i in lst:
#     if type(i) == tuple:
#         break
#     count = count + 1
# print(count)

ctr = 0
for n in lst:
    if isinstance(n,tuple):
        break
    ctr += 1
print(ctr)





