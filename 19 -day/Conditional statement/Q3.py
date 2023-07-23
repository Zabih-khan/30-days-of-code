#Write a python programm to guess a number between 1 to 9:
import random

target_num  = random.randint(1,10)
guess_num = 0
while target_num != guess_num:
    guess_num = int(input("Guess a number."))
print("Well guessed")

# while True:
#
#     lst = []
#     for i in range(1,9):
#         lst.append(i)
#     rad  = random.choice(lst)
#     user = int(input("Emter the number."))
#     if user == rad:
#         print("You won")
#         break
#
#     else:
#         print("Lose.")




















