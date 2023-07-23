# Enter your code here. Read input from STDIN. Print output to STDOUT
dic={}



n=int(input())
for i in range(n):
    data=list(input().split())
    dic[data[0]]=data[1]
    
while True:
    try:
        
        name=input()
        if name in dic:
            print(name+"="+dic[name])
            
        else:
            print("Not found")
    except:
        break
