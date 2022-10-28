s=str(input())
a=list(s.split(" "))
c=[]
for i in a:
    d=min(i)
    e=max(i)
    f=abs(ord(d)-ord(e))
    c.append(f)
print(*c)