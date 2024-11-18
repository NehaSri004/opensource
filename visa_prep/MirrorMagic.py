n = int(input())
arr = []
for i in range(n):
    x = list(map(int, input().split()))
    y = []
    for j in range(n-1, -1, -1):
        y.append(x[j])
    arr.append(y)
for i in arr:
    print(" ".join(map(str, i)))
