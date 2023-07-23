class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next
    def insert(self,head,data):
        node=Node(data)
        if head is None:
            return node
        else:
            curr = head
            while curr.next:
                curr = curr.next
            curr.next = node
        return head
        
mylist= Solution()
T=int(input("How many node you want to insert:"))
head=None
for i in range(T):
    data=int(input("Enter data:"))
    head=mylist.insert(head,data)    
mylist.display(head); 	  
