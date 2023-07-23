a = [  ('f',9) , ('z',2) , ( 't', 4) , ('x', 8) ,('b',1) , ("m",7)]
#first
a.sort()
print( a )

#second
a.sort(key = lambda a: a[1])


#This will print the element from the list according to their size.
lst = ["zabih","umair","khan","ali"]
lst.sort(key=lambda x: len(x))
print(lst)

