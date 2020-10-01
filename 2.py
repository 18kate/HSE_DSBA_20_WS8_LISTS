a1=input().split()
a=list(map(int,a1))

b1=input().split()
b=list(map(int,b1))

x=set(a)
y=set(b)

if x==y:
    print('YES')
else:
    print('NO')
