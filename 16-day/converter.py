with open("par.txt") as f:
    lines=f.readlines()
currencyDict={}
for line in lines :
    parsed=line.split("\t")
    currencyDict[parsed[0]]=parsed[1]


amount=int(input("Enter amount:"))
print("Enter the name of currency you want to convert this amount to ? Available option:")

[print(item) for item in currencyDict.keys()]
currency=input("please enter one of these values")
print(f"{amount} INR is equal to {amount *float(currencyDict[currency])}{currency}")
