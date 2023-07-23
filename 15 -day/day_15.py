sum=0
while True:
    userinput=input("Enter the item price or press q to Quite:")
    if (userinput!='q'):
        sum=sum+int(userinput)
        print(f"Order total so far: {sum}")        
        
    
    else:
        print(f"Your total price is {sum}.Thanks for shopping with us: ")
        break
