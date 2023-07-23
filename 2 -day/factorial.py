def factorial(n):
    if n==0:
        return 1
    return n* factorial(n-1)
x="y"
while x=="y":
    x=int(input("Enter the number:"))
    print(factorial(x))
    print()
    x=input("Another Number?y/n")
