s=[(10, 20, 40), (40, 50, 60), (70, 80, 90)]
x=100
q=[]
for i in range(len(s)):
    w=list(s[i])
    w[len(w)-1]=x
    q.append(tuple(w))
print(q)
