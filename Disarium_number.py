n=int(input())
a=str(n)
b=int(a[::-1])
d=b
s=0
r=0
i=1
while b>0:
    r=b%10
    s+=(r**i)
    b=b//10
    i=i+1
if int(a)==s:
    print("True")
else:
    print("False")