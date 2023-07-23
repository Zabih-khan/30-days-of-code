class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def creatNode(self, data):
        return Node(data)

    def insert(self,node,data):
        if node is None:
            return self.creatNode(data)
        if data < node.data:
            node.left = self.insert(node.left,data)
        else:
            node.right = self.insert(node.right,data)
        return( node)

    def inorder_Traversal(self , root):
        if root is not None:
            self.inorder_Traversal(root.left)
            print(root.data)
            self.inorder_Traversal(root.right)

    def preorder_Traversal(self , root):
        if root is not None:
            print(root.data)
            self.preorder_Traversal(root.left)
            self.preorder_Traversal(root.right)
    def postorder_Traversal(self,root):
        if root is not None:
            self.postorder_Traversal(root.left)
            self.postorder_Traversal(root.right)
            print(root.data)

    def Height(self,root):
        if root is None:
            return -1
        else:
            return max(self.Height(root.left),self.Height(root.right)) + 1

t = Tree()
root = t.creatNode(100)
t.insert(root,50)
t.insert(root,200)
t.insert(root,300)
t.insert(root,20)
t.insert(root,150)
t.insert(root,70)
t.insert(root,180)
t.insert(root,120)
t.insert(root,30)
print('inorder Traversal')
t.inorder_Traversal(root)
print()

print('preorder Traversal')
t.preorder_Traversal(root)
print()

print('postorder Traversal')
t.postorder_Traversal(root)
# print()
# print('Maximum Height of the tree is:',end=' ')
# print(t.Height(root))

