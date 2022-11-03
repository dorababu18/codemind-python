import math as m
def prime(a):
    if a==1:
        return 0
    for i in range(2,int(m.sqrt(a)+1)):
        if a%i==0:
            return 0
    return 1
n=int(input())
for _ in range(n):
    a=int(input())
    b=a
    while b:
        b=b+1
        if prime(b):
            break
    c=b
    while c:
        c=c-1
        if prime(c):
            break
    if b-a<a-c:
        print(b)
    else:
        print(c)
