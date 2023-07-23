class Queue:
    def __init__(self):
        self._qlist = list()

    def isEmpty(self):
        print(len(self._qlist) == 0)
        print()

    def __len__(self):
        print('Length of the queue is :',len(self._qlist))

    def Enqueue(self,item):
        self._qlist.append(item)

    def Dequeue(self):
        assert not self.isEmpty(),'Cannot dequeue from empty queue'
        x = self._qlist.pop(0)
        print(x,'is removed:')
        print()

    def display(self):
        print(self._qlist)

obj = Queue()
obj.Enqueue(4)
obj.Enqueue(5)
obj.Enqueue(1)
obj.Enqueue(9)
obj.Enqueue(0)
obj.Enqueue(4)
obj.Enqueue(1)
obj.display()
obj.__len__()
obj.Dequeue()
print("New Queue:")
obj.display()

