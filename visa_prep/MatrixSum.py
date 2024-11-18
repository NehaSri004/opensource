n = int(input())
rows = []
cols = []
arr = []
for i in range(n):
    x = list(map(int, input().split()))
    arr.append(x)
    rows.append(sum(x))
for i in zip(*arr):
    cols.append(sum(i))
for i in range(n):
    print(rows[i]+cols[i],end=" ")
