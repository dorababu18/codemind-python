import math
n=int(input())
for i in range(1,int(math.sqrt(n)+1)):
    if ((i**2)*(i+1)**2==n) or i*i==n:
        print("True")
        break
else:
    print("False")