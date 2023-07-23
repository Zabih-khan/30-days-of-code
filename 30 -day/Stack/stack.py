stk = []
class stack:
    #----------push element------------
    def Push(self, num):
        self.num = num
        stk.append(self.num)

    #----------pop element------------
    def Pop(self):
        stk.pop()
    # ----------Display element.------------
    def Display(self):
        print("The Elements in the stack is.")
        print(stk)

    #----------Top element.------------
    def GetTop(self):
        peek = len(stk) - 1
        print("Top element in the stack is:", stk[peek])

    #----------Mid element.------------
    def middleitem(self):
            i = len(stk)//2
            print('Mid element in the stack is.',stk[i])
    # ----------Is stack empty or not.------------
    def IsEmpty(self):
        if len(stk) == 0:
            print("Stack is Empty.")
            print(stk)

    # ----------Is stack full or not.------------
    def IsFull(self):
        if len(stk) != 0:
            print("Stack is Full.")


if __name__ == '__main__':
    obj = stack()
    a = int(input("Enter the number:"))
    b = int(input("Enter the number:"))
    c = int(input("Enter the number:"))
    d = int(input("Enter the number:"))
    e = int(input("Enter the number:"))
    f = int(input("Enter the number:"))
    print("Elements is sucessfully pushed:")
    obj.Push(a)
    obj.Push(b)
    obj.Push(c)
    obj.Push(d)
    obj.Push(e)
    obj.Push(f)
    obj.Pop()
    obj.Display()
    obj.GetTop()
    obj.middleitem()
    obj.IsEmpty()
    obj.IsFull()

