def factorail(n):
    if n == 1 or num == 0:
        return 1
    else:
        return n * factorail(n-1)

def trail(number):
    count = 0
    i = 5
    while (number // i !=0):
        count = count + int(number/i)
        i = i * 5
    return f"There are {count}  zero in the last."


if __name__ == '__main__':
    num = int(input("Enter the numbers"))
    print(factorail(num))
    print(trail(num))

