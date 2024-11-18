x, n = map(int, input().split())
if x*100 >= n:
    print(0)
else:
    rem = n-x*100
    if rem%100==0:
        print(rem//100)
    else:
        print(rem//100+1)
