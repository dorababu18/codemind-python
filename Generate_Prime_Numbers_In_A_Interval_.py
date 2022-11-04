import math as m
n=int(input())
m=int(input())
for i in range(n,m):
    if i>1:
        for j in range(2,int(i**0.5)+1):
            if i%j==0:
                break
        else:
            print(i)