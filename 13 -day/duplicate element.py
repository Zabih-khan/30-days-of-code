#Find the first duplicate elements in a array of integer:

def duplicate(lst):
    num_set=set()
    for i in range(len(lst)):
        if lst[i] in num_set:
            return "The duplicate number is :",lst[i]
        else:
            num_set.add(lst[i])
    return "There is no duplicate in the list:"

#Here we create a list
n=int(input("How many time Do you want to iterate:"))
for i in range(n):
    lst=list(map(int,input("Enter numbers:").rstrip().split()))
    print(duplicate(lst))
