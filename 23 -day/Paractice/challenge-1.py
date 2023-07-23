count = 0
while True:
    name = 'zabih'
    count = count + 1
    if count == 4:
        break
    userinput = input("Enter the name.")
    if userinput == name:
        print("You won.")
        break
    else:
        print("you Lose")