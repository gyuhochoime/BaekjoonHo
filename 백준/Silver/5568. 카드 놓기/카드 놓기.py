import sys
from itertools import permutations
n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
arr = [sys.stdin.readline().rstrip() for _ in range(n)]
num = list(permutations(arr, k))
tmp = []
for i in num:
    tmp.append("".join(map(str, i)))
tmp = set(tmp)
print(len(tmp))
