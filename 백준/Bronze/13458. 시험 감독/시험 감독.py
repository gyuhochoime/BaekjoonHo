import sys
n = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
a, b = map(int, sys.stdin.readline().rstrip().split())
cnt = n
for i in arr:
    su = i
    su -= a
    if su > 0:
        if su % b == 0:
            cnt += su // b
        else:
            cnt += su // b + 1
print(cnt)
