import sys
from itertools import combinations
n, m = map(int, sys.stdin.readline().split())
arr = list(sys.stdin.readline().split())
arr.sort()
moum = ["a", "e", "i", "o", "u"]
lst = list(combinations(arr, n))
for i in lst:
    cnt = 0
    for j in i:
        if j in moum:
            cnt += 1
    if cnt > 0 and n - cnt > 1:
        for j in i:
            print(j, end = "")
        print()
