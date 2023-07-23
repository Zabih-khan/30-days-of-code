#Write a python program to remove an empty tuple from a list of tuples

lst= [(),(),(),(1,2),(5,6),('a',1),()]
l = [i for i in lst if i]
print(l)


