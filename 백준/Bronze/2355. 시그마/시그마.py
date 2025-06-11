import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
start = min(n, m)
end = max(n, m)
cnt = (start + end) * (end - start + 1) // 2
print(cnt)
