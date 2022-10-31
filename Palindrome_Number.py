n=int(input())
for _ in range(n):
    a=int(input())
    b=str(a)
    c=b[::-1]
    if a==int(c):
        print("True")
    else:
        print("False")
    
