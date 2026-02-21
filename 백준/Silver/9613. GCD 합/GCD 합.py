import sys
import math
T = int(sys.stdin.readline())
for _ in range(T):
    arr = list(map(int, sys.stdin.readline().split()))
    tot = 0
    for i in range(1, arr[0] + 1):
        for j in range(i + 1, arr[0] + 1):
            tot += math.gcd(arr[i], arr[j])
    print(tot)
