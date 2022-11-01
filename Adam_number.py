n=int(input())
a=n*n
b=str(n)
c=b[::-1]
d=int(c)*int(c)
e=str(d)
f=int(e[::-1])
if a==f:
    print("True")
else:
    print("False")