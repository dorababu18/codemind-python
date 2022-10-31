n=int(input())
for _ in range(n):
    a=int(input())
    for i in range(1,int(a**0.5)+1):
        if i*i==a:
            print("True")
            break
    else:
        print("False")