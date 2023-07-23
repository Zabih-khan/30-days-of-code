
def nsplit(n, s):
    l2 = []
    s2 = ''
    c = 0
    for i in range(len(s)):
        s2 += s[i]
        c=c + 1
        if c==n or i==len(s)-1:
            l2.append(s2)
            s2=''
            c=0
    return l2
s = "Muhammad Umair"
print(nsplit(1, s),'\n')
print(nsplit(2, s),'\n')
print(nsplit(3, s),'\n')
print(nsplit(4, s),'\n')
print(nsplit(5, s),'\n')
print(nsplit(6, s),'\n')
print(nsplit(7, s),'\n')
print(nsplit(8, s),'\n')
print(nsplit(9, s),'\n')
print(nsplit(10, s),'\n')
print(nsplit(11, s),'\n')
print(nsplit(12, s),'\n')
print(nsplit(13, s),'\n')
print(nsplit(14, s),'\n')
