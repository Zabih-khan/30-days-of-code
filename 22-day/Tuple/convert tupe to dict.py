tuple = ((2,4),(4,6),(1,4))
# dic = dict()
# for x,y in tuple:
#     dic[y]= (x)
# print(dic)
#
# print(dict((y,x)for x,y in tuple))

d = [(y, x)for x,y in tuple]


print(d)