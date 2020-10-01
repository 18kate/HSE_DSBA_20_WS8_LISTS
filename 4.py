a1=input().split()
a=list(a1)
b=''.join(a)
q=a[0]
s=[]
for i in a:
        if q!=i:
           s.append(q)
        q=i
for i in a:
    if i not in s:
        s.append(i)
print(s)
