import math as m
def prime(a):
    if a==1:
        return 0
    for i in range(2,int(m.sqrt(a)+1)):
        if a%i==0:
            return 0
    return 1
n=int(input())
while n:
    n=n+1
    if prime(n):
        b=str(n)
        c=b[::-1]
        if int(c)==int(b):
            break
print(int(c))
            
            