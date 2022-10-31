import math
def ispr(a):
    if a<=1:
        return False
    for i in range(2,int(math.sqrt(a)+1)):
        if a%i==0:
            return False
    return True
a=int(input())
b=int(input())
c=0
for i in range(a,b+1):
    if ispr(i):
        c+=1
print(c)