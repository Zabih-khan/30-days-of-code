from array import *

a = [2,4,5]
if not a:
    print("Empty")
else:
    print("Element is present;")
print()

print("***********************************")
#Write a python programm to remove the first element fron the array:
arr = [2,3,4,5,6]
print("Original array:",arr)
x = arr.pop(2)
print("New array:",arr)
print()

print("***********************************")
#Write a python programm to insert a new item before the second element in an existing array
arr = [1,2,3]
print("Original array:",arr)
arr.insert(1,4)
print("New array:",arr)
print()

print("***********************************")
#write a python programm to append items from inerrable to the end of the array:
arr = [2,3,4,5]
print("Original array:",arr)
arr.append(8)
print("New array:",arr)

print("***********************************")
#write a python program to covert an array to an ordinary lsit with the same item
print()
arr = array('i',[1,3,5,3,7,1,9])
print("Original array:",arr)
print(type(arr))
print()
list = arr.tolist()
print("Convert the said item to an ordinary list with the same items")
print(list)
print(type(list))
print()

print("***********************************")
#write a python program to get the current memory address and
# the length in elements of the buffer used to hold an array
# content and also find size of the memory buffer in bytes.

arr = array("i",[3,4,5,6])
print("Original Array:",arr)
print("current memeory address and length of the element in array")
print(arr.buffer_info())
print("Size of the memory in bytes:")
print(arr.buffer_info()[1] * arr.itemsize)
print()

print("***********************************")
# python programm to find the first duplicate
# element in a given array of integer
arr = [2,2,3,4,5,3,4]
arr_set = set()
for i in arr:
    if i in arr_set:
        print(i)
    else:
        arr_set.add(i)






