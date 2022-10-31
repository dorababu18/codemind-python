import math
a=int(input())
b=int(input())
for i in range(a,b):
    if i>1:
        for j in range(2,int(math.sqrt(i)+1)):
            if i%j==0:
                break
        else:
            print(i)
        