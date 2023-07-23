def isEmpty(s):
    if len(s) == 0:
        return True
    else:
        return False

def push(s,item):
    s.append(item)
    top = len(s) -1

def display(s):
    if isEmpty(s):
        print("Stack is empty")
    else:
        print(s)
        # top = len(s) -1
        # print(s[top],'<----top')
        # for x in range(top-1,-1,-1):
        #     print(s[x])

#main
stk = []
top = None
bokno = int(input("Enter the book no."))
bokname = input('Enter the book name')
i = [bokno,bokname]
push(stk,i)
bokno = int(input("Enter the book no."))
bokname = input('Enter the book name')
i = [bokno,bokname]
push(stk,i)
display(stk)

# while True:
#     print("Stack implementation")
#     print('1.Push')
#     print('2.Display')
#
#     ch = int(input('Enter your choice.'))
#     if ch == 1:
#         bookno = int(input("Enter the book number."))
#         bookname  = input("Enter the boook name.")
#         i = [bookno,bookname]
#         push(stk,i)
#     if ch== 2:
#         display(stk)



