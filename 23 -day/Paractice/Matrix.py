a=[]
x=int(input('enter number of rows in odd for square matrix:'))
i=0
k=x//2
for i in range(x):
    b = []
    for j in range(x):
        b.append('.')
    a.append(b)

row=0
for i in a:
    col=0
    n=x
    for j in i:
        if row==k or col==k:
            a[row][col]='*'
        elif row==col:
            a[row][col]='*'
            a[row][n-1]='*'
        col+=1
        n-=1
    row+=1
for i in a:
    for j in i:
        print(j,end='\t')
    print('\n')