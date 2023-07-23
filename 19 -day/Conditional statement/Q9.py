#Write a python program whick iterate the integer from 1 to 50 for multiple of
#three print FIZZ instead of the number and for the multiple of five print BIZZ
#for a number which are multiple of both three and five print FIZZBUZZ

for i in range (51):
    if i % 3 == 0 and i % 5 == 0:
        print("FIZZBUZZ")
        continue
    elif i % 3 == 0:
        print("FIZZ")
        continue
    elif i % 5 == 0:
        print("BUZZ")
        continue
    print(i)
