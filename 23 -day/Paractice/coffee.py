coffee = ["Café Latte", "Caffe Americano", "Espresso", "Cappuccino", "Macchiato"]

choice = int(input("put index of the list item."))

try:

    print(coffee[choice])

except:
    if choice >= 5:
        print("Invalid number")

finally:
    print("Have a good day")
