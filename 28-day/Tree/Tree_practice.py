class Node:
    def __init__(self,data):
        self.data = data
        self.left_child = None
        self.right_child = None

class Tree:
    def __init__(self):
        self.root_node = None

    def insert(self,data):
        node = Node(data)
        if self.root_node is None:
            self.root_node = node
        else:
            current = self.root_node
            parent = 0
            while current is not None:
                parent = current
                if node.data < current.data:
                    current = current.left_child
                    if current is None:
                        parent.left_child = node
                else:
                    current = current.right_child
                    if current is None:
                        parent.right_child = node

t = Tree()
n1= Node(10)
t.root_node = n1
for i in [3,4,5,6,7,8,9,0,6]:
    t.insert(i)
current = n1
while current:
    print(current.data)
    current = current.left_child




