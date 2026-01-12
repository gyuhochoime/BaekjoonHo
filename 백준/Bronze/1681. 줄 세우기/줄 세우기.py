import sys
n, m = map(str, sys.stdin.readline().rstrip().split())
su = [0] * 2000001
for i in range(2000001):
    if m in str(i):
        su[i] = 1
cnt = int(n)
tmp = 0
for i in range(1, 2000001):
    if su[i] == 0:
        cnt -= 1
        tmp = i
    if cnt == 0:
        break
print(tmp)
