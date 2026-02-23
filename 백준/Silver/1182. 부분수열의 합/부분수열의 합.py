import sys
def solve(a):
    global cnt
    if sum(tmp) == m and tmp:
        cnt += 1
    for i in range(a, n):
        tmp.append(arr[i])
        solve(i + 1)
        tmp.pop()
n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
cnt = 0
tmp = []
solve(0)
print(cnt)
