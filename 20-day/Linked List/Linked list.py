class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linked_list:

    def __init__(self):
        self.head = None

    def traversal(self):
        curNode = self.head
        while curNode is not None:
            print(curNode.data, end=' ')
            curNode = curNode.next

    def insert_b(self, data):
        nb = Node(data)
        nb.next = self.head
        self.head = nb

    def insert_e(self, data):
        ne = Node(data)
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = ne

    def insert_position(self, pos, data):
        np = Node(data)
        temp = self.head
        for i in range(pos - 1):
            temp = temp.next
        np.data = data
        np.next = temp.next
        temp.next = np

    def unordersearch(self, target):
        curNode = self.head
        while curNode is not None and curNode.data != target:
            curNode = curNode.next
        print(curNode is not None)

    def remove(self, target):
        preNode = None
        curNode = self.head
        while curNode is not None and curNode.data != target:
            preNode = curNode
            curNode = curNode.next
        if curNode is not None:
            if curNode is self.head:
                self.head = curNode.next
            else:
                preNode.next = curNode.next

L = Linked_list()
n1 = Node(2)
L.head = n1

n2 = Node(3)
n1.next = n2

n3 = Node(6)
n2.next = n3
L.insert_b(8)
L.insert_e(10)
L.insert_position(3, 67)
print('Check element is present or not.[True/False]')
L.unordersearch(67)
L.traversal()
print()
print("After remove the value fron the linked list.")
L.remove(10)
L.traversal()