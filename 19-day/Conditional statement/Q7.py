#Write a python program that print all the numbers from
# 0 to 6 except 3 and 6
for i in range(0,6+1):
    if i == 3 or i == 6:
        continue
    print(i)
