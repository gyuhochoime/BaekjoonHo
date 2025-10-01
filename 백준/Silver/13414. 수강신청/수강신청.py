import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
seq = dict()
for i in range(1, m + 1):
    a = sys.stdin.readline().rstrip()
    seq[a] = i
arr = [(hak, rank) for hak, rank in seq.items()]
arr.sort(key = lambda x: (x[1]))
for hak, rank in arr:
    if n == 0:
        break
    print(hak)
    n -= 1
