a1=input().split()
a=list(a1)
b=''.join(a)

x=int(input())
s=[]
m=1+(len(a)//x)
print(m)
for i in range(len(a)+1):
    s.append(a[i])
    for s in a:
        s.append(s.remove())
    if len(s)==x:
        print(s)
        s=[]

