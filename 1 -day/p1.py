class Node:
    def __init__(self,data):
        self.left=None
        self.data=data
        self.right=None
class Tree:
    def createNode(self,data):
        return Node(data)

    def insert(self,node,data):
        if node is None:
            return self.createNode(data)

        if data<node.data:
            node.left=self.insert(node.left,data)

        if data>node.data:
            node.right=self.insert(node.right,data)
        return node
    def height(self,root):
        if root is None:
            return -1
        return max(self.height(root.left),self.height(root.right))+1
    
    def Traversal_inorder(self,root):
        if root is not None:
            self.Traversal_inorder(root.left)
            print(root.data)
            self.Traversal_inorder(root.right)
            
    def Traversal_level(self,root):
        q=[]
        q.append(root)
        while len(q)!=0:
            root=q.pop(0)
            print(root.data)
            if root.left is not None:
                q.append(root.left)
            if root.right is not None:
                q.append(root.right)
                
    def check_bst(self,root):
        def inorder(root,values):
            if root is None:
                return
            
            inorder(root.left,values)
            values.append(root.data)
            inorder(root.right,values)
        values=[]
        inorder(root,values)
        for i in range(len(values)-1):
            if values[i]>=values[i+1]:
                return False
        return True
            
        

        
    
tree=Tree()
root=tree.createNode(3)
tree.insert(root,2)
tree.insert(root,45)
tree.insert(root,21)
tree.insert(root,12)
tree.insert(root,34)
tree.insert(root,4)
tree.insert(root,5)
tree.insert(root,26)
tree.insert(root,27)
tree.insert(root,9)
tree.Traversal_inorder(root)
print()
print("Height")
print(tree.height(root))
print("Traversal_level")
tree.Traversal_level(root)
print("Check BST")
print(tree.check_bst(root))

            
