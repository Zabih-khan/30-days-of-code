#Write a python program to count the number of even and odd numbers from a series of number:

lst = [2,3,4,5,6,7,8,9,1]
Even_count = 0
Odd_count = 0
for i in lst:
    if i % 2 == 0:
        Even_count = Even_count + 1
    else:
        Odd_count = Odd_count + 1
print(Even_count)
print(Odd_count)


