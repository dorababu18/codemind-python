t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    d=0
    for i in range(a,b+1):
        c=str(i)
        if int(c[-1])==2 or int(c[-1])==3 or int(c[-1])==9:
            d+=1
    print(d)
            