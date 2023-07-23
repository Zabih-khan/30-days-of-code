#Write a python program that get the fibonaci series between 0 to 50.
x = 0
y = 1
z = 0
for i in range(0,5):
    x = y
    y = z
    z = x + y
    print(z)


#using while loops.
# n = int(input("Enter the numbers."))
# while (z <= n):
#     print(z)
#     x = y
#     y = z
#     z = x + y


