s=str(input())
b=0
for i in s:
    if int(i)%2!=0:
        b=int(i)*int(i)
        print(b,end="")