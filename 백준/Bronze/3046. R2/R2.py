import sys

n, m = list(map(int ,sys.stdin.readline().rstrip().split()))
k = 2 * m - n
print(k)
