n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
t =[list(x) for x in zip(*arr)]
for x in t:
    print(" ".join(map(str, x)))
