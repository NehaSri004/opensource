n = int(input())
arr = list(map(int, input().split()))
s = ""
for x in arr:
    s+=str(x)
s = s.split('1')
m = 0
for x in s:
    m = max(m, len(x))
print(m)
