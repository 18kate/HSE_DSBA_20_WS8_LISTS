s=input().split()
l=list(map(int,s))
m=1
print(l)
for i in range (len(l)):
    m*=l[i]
print(m)
