total = 0
while True:
    num = input ("Enter num or type '-->done<--' to calculate ;\n")
    if num == "done":break
    value = int(num)
    total = total + value

print(total)
