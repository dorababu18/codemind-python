n=int(input())
if n<0:
 a=n*-1
 b=str(a)
 c=b[::-1]
 print(-1*int(c))
else:
    b=str(n)
    c=b[::-1]
    print(int(c))
