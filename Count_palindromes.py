n=int(input())
l=list(map(int,input().split()))
c=0
for i in range(n):
    if str(l[i])[::-1]==str(l[i]):
        c+=1
print(c)