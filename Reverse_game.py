n=int(input())
l=list(map(int,input().split()))
a=[]
b=0
c=0
for i in range(n):
    b=str(l[i])[::-1]
    c=int(b)
    a.append(c)
print(*a)
    