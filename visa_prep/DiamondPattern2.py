n = int(input())
for i in range(n):
    print("*"*(i+1)+" "*(2*(n-1-i))+"*"*(i+1))
for i in range(1, n):
    print("*"*(n-i)+" "*(2*i)+"*"*(n-i))
