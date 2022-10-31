import math
n=int(input())
for i in range(1,int(math.sqrt(n)+1)):
    if i*(i+1)==n:
        print("YES")
        break
else:
    print("NO")