n = int(input())
arr = list(map(int, input().split()))
res = []
for i in range(0,n):
    res.append(abs(sum(arr[:i])-sum(arr[i+1:])))
print(" ".join(map(str, res)))
