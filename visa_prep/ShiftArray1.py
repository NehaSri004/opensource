n = int(input())
arr = list(map(int, input().split()))
res = []
for i in range(1, n):
    res.append(arr[i])
res.append(arr[0])
print(" ".join(map(str, res)))
