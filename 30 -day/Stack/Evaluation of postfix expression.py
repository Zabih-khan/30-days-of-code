def eval_expression(arr):
    stack = []
    operator=["+","-","*","/","%"]

    for ch in arr:
        if ch not in operator:
            stack.append(ch)
        else:
            first = int(stack.pop())
            sec = int(stack.pop())
            if ch == "+":
                x = first + sec
                stack.append(x)

            if ch == "-":
                x = first - sec
                stack.append(x)

            if ch == "*":
                x = first * sec
                stack.append(x)

            if ch == "/":
                x = first / sec
                stack.append(x)

            if ch == "^":
                x = first ^ sec
                stack.append(x)

            if ch == "%":
                x = first % sec
                stack.append(x)
    return stack[-1]

A =   ["2", "1", "+", "3", "*" ]
print(eval_expression(A))