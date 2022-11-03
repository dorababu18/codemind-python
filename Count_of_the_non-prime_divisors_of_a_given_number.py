import math as m
def prime(a):
    if a==1:
        return 0
    for i in range(2,int(m.sqrt(a)+1)):
        if a%i==0:
            return 0
    return 1
n=int(input())
b=[]
c=0
for i in range(1,n+1):
    if n%i==0:
        b.append(i)
for j in b:
    if prime(j)==0:
        c+=1
print(c)
