n = int(input())
arr = list(map(int, input().split()))
k = int(input())
rem = k%n
if rem==0:
    print(" ".join(map(str, arr)))
else:
    arr = arr[n-rem:]+arr[:n-rem]
    print(" ".join(map(str, arr)))
