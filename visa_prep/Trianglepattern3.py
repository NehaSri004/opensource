n = int(input())
for i in range(0,n):
    x = 0
    for j in range(i+1):
        x=x+1
        print(x,end="")
    print(((n-1-i)*2)*" ",end="")
    for j in range(i+1):
        print(x,end="")
        x=x-1
    print()
