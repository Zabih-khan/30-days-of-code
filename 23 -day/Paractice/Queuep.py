a=[1,2,3]
b=[4,5,6]
c=[7,8,9]
queue=[]
k=0
i=0
j=0
while i<len(a):
   j=i
   k=i
   queue.append(a[i])
   queue.append(b[j])
   queue.append(c[k])
   i+=1
print(queue)
print("De queue")


#Using for loops
# queue = []
# a = [1,2,3]
# b = [6,7,7]
# c = [3,4,5]
#
# for i in (a):
#     queue.append(i)
# for j in (b):
#     queue.append(j)
# for k in (c):
#     queue.append(k)
#
# print(queue)