import random
list = [1,2,3,4,5,6,7,8,9]
rand = random.choice(list)

for i in range(3):
    userinput = int(input("Enter the your choice."))
    if rand == userinput:
        x = "you won the game:"
        print(x)
        break
    else:
        print("You lose! Please try again.")

print()
print("Thank you for playing game.........")
print()
