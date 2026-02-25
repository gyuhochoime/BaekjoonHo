import sys
n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
prefix = [0] * n
prefix[0] = arr[0]
cnt = 0
for i in range(1, n):
    prefix[i] = prefix[i-1] + arr[i]
for i in range(n):
    if prefix[i] == m:
        cnt += 1
    for j in range(i):
        if prefix[i] - prefix[j] == m:
            cnt += 1
            break
        elif prefix[i] - prefix[j] < m:
            break
print(cnt)
