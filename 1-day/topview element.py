class Node:
    def __init__(self,data):
        self.data=data
        self.left =None
        self.right=None
        self.level=None
class Tree:
    def creatNode(self,data):
        return Node (data)

    def insert(self,node,data):
        if node is None:
            return self.creatNode(data)
        if data <node.data:
            node.left=self.insert(node.left,data)
        if data>node.data:
            node.right=self.insert(node.right,data)
        return node
    def topview(self,root):
        q=[]
        d=dict()
        root.level=0
        q.append(root)
        while len(q)!=0:
            root=q.pop(0)
            if root.level not in d:
                d[root.level]=root.data
            if root.left is not None:
                q.append(root.left)
                root.left.level=root.level-1
            if root.right is not None:
                q.append (root.right)
                root.right.level=root.level+1
                
        print("These are the topview elements:")
        print(*d.values())
 
tree=Tree()
root=tree.creatNode(4)
tree.insert(root,3)
tree.insert(root,10)
tree.insert(root,21)
tree.insert(root,32)
tree.insert(root,30)
tree.insert(root,9)
tree.insert(root,2)
tree.insert(root,6)
tree.topview(root)
