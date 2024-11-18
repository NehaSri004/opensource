n = int(input())
arr = list(map(int, input().split()))
uni = []
for x in arr:
    if x not in uni:
        uni.append(x)
print(" ".join(map(str, uni)))
