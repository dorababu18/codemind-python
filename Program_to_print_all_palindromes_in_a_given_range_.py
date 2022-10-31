a=int(input())
b=int(input())
for i in range(a,b):
    c=str(i)
    d=c[::-1]
    if c==d:
        print(i,end=" ")