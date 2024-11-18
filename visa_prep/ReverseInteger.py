n = int(input())
sign = -1 if n<0 else 1
n = abs(n)
rev = int(str(n)[::-1])
rev *= sign
m1 = -2**31
m2 = 2**31-1
if rev<m1 or rev>m2:
    print("0")
else:
    print(rev)
