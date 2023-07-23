output = []
operator = []
priority = {"(":0,"+":1,"-":1,"*":2,"/":2,"^":3}
exp = "( (A * B) + (C / D) )"
for ch in exp:
    #This for paranthesis
    if ch == "(":
        operator.append(ch)
    elif ch == ")":
        #pop one by one operator from operator stack and push
        # that opeator into the output stack until open parantesis appear.
        while operator[-1] != "(":
            ele = operator.pop()
            output.append(ele)
        operator.pop()

    #This for operator
    elif ch == "^" or ch == "+" or ch == "-" or ch == "*" or ch == "/":
        #First check operator stack should not empty.
        if len(operator) > 0:
            while priority[operator[-1]] >= priority[ch]:
                ele = operator.pop()
                output.append(ele)
                if len(operator) == 0:
                    break
        operator.append(ch)
    #This for operant
    else:
        output.append(ch)
#Check operator stack is empty or Not after scanning complate expression
while len(operator)!= 0:
    ele = operator.pop()
    output.append(ele)
#Now print output stack
print("Infix expression: " + str(exp))
print("Postfix expression: " + str(),end = "")
for i in output:
    print(i,end="")
