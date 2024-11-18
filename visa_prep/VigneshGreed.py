n = int(input())
flag = -1
arr = sorted(list(map(int, input().split())))
for i in range(n-1, 1, -1):
    if arr[i] < arr[i-1] + arr[i-2]:
        flag = 1
        print(arr[i]+arr[i-1]+arr[i-2])
        break
if flag==-1:
    print(-1)
