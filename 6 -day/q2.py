# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
for z in range(n):
    string=list(input())
    for i in range(len(string)):
        if i%2==0:
            print(string[i],end='')
            
    print(' ',end="")        
    for i in range(len(string)):
        if i%2!=0:
            print(string[i],end='')


    print()
    
    

    
