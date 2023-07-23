count = 0
total = 0
while True:
    num = input("Enter the number or type 'done' to calculate the average :")
    if num == "done":
        break
    else:
        value = int(num)
        total = total + value
        count = count +1
aver = total / count
print("The average of these numbers is.",aver)