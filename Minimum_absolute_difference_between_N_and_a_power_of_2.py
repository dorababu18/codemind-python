n=int(input())
a=[]
for i in range(1,n):
    b=2**i
    c=abs(n-b)
    a.append(c)
print(min(a))