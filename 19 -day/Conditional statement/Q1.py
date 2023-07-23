#Write a python program to find those nubmers which are divisible by 7 and multiple of 5,
#between 1500 and 2700 (both included)
n1 = []
for i in range(1500,2700):
    if i%7 == 0 and i%5 == 0:
        n1.append(str(i))
print(",".join(n1))