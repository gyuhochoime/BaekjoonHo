import sys
import itertools as it
n = int(sys.stdin.readline().rstrip())
a = [i for i in range(1, n + 1)]
for p in it.permutations(a):
    print(*p)
