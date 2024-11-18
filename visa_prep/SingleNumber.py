n = int(input())
arr = list(map(int, input().split()))
for x in arr:
    if arr.count(x)==1:
        print(x)
        break
