import sys
import math
n = int(sys.stdin.readline().rstrip())
for _ in range(n):
    maxi = 0
    arr = list(map(int, sys.stdin.readline().rstrip().split()))
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            a = math.gcd(arr[i], arr[j])
            if a > maxi:
                maxi = a
    print(maxi)
