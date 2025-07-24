import sys
T = int(sys.stdin.readline())
arr = []
for _ in range(T):
    s, e = map(int, sys.stdin.readline().split())
    arr.append((s, e))

left = max(s for s, e in arr)
right = min(e for s, e in arr)

print(max(0, left - right))
