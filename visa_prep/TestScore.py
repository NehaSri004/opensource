n, x, y = map(int, input().split())
if (y%x==0) and (n*x>=y):
    print("YES")
else:
    print("NO")
