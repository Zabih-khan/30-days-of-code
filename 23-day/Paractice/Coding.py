class programer:
    def code(self):
        print("Keep coding")

    def drink_coffee(self):
        print("Drink coffe to fresh your mind")

    def Take_sleep(self):
        print("Take break to decrease your tired.")


x = "fresh"
y = "tired"
z = "awake"
pro = programer()

if z == "awake":
    pro.code()

if x == "fresh":
    pro.drink_coffee()

elif y == "tired":
    pro.Take_sleep()

if __name__ == '__main__':
    pass
