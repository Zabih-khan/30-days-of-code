class Node:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None
class Tree:
    def __init__(self):
        self.root_node = None

    def find_min(self):
        current = self.root_node
        while current.left_child:
            current = current.left_child
        return (current.data)

    def insert(self, data):
        node = Node(data)
        if self.root_node is None:
            self.root_node = node
        else:
            current = self.root_node
            parent = None
            while current is not None:
                parent = current
                if node.data < current.data:
                    current = current.left_child
                    if current is None:
                        parent.left_child = node
                        return node
                else:
                    current = current.right_child
                    if current is None:
                        parent.right_child = node
                        return node
    def get_node_with_parent(self, data):
        parent = None
        current = self.root_node
        if current is None:
            return (parent, None)
        while True:
            if current.data == data:
                return (parent, current)
            elif current.data > data:
                parent = current
                current = current.left_child
            else:
                parent = current
                current = current.right_child
        return (parent.data, current.data)

    # def remove(self, data):
    #     parent, node = self.get_node_with_parent(data)
    #     if parent is None and node is None:
    #         return False
    #     # Get children count
    #     children_count = 0
    #     if node.left_child and node.right_child:
    #         children_count = 2
    #     elif (node.left_child is None) and (node.right_child is None):
    #         children_count = 0
    #     else:
    #         children_count = 1
    #     if children_count == 0:
    #         if parent:
    #             if parent.right_child is node:
    #                 parent.right_child = None
    #             else:
    #                 parent.left_child = None
    #         else:
    #             self.root_node = None
    #
    #     elif children_count == 1:
    #         next_node = None
    #         if node.left_child:
    #             next_node = node.left_child
    #
    #
    #     else:
    #         next_node = node.right_child
    #     if parent:
    #         if parent.left_child is node:
    #             parent.left_child = next_node
    #         else:
    #             parent.right_child = next_node
    #     else:
    #         self.root_node = next_node





    def inorder(self, root_node):
        current = root_node
        if current is None:
            return
        self.inorder(current.left_child)
        print(current.data, end= " ")
        self.inorder(current.right_child)



t = Tree()
n1 = Node(10)
t.root_node = n1
for x in [7, 6, 8, 5, 9, 2, 12, 3]:
    t.insert(x)
t.inorder(n1)
print()
current, parent  = t.get_node_with_parent(3)
print(current.data,parent.data)
print()
print(t.find_min())








