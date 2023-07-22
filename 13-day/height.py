class student:
    def __init__(self,name,height):
        self.name=name
        self.height=height
    # This function concatenate name and height
    def __str__(self):
        return self.name +":"+ str(self.height)
    
#Defining a function to built a menu:    
def heightrecord(rec,name,height):
    rec.append(student(name,height))
    return rec
record=[]
x="y"
while x=="y":
    name=input("Enter name:")
    height=int(input(f"Enter the height of the {name}:"))
    record=heightrecord(record,name,height)
    x=input("Another student ? y/n")
    
n=1
for i in record:
    print(n,".",i)
    n=n+1
    


    

    
