import sys
n = int(sys.stdin.readline().rstrip())
cnt = 1
for i in range(n, 0, -1):
    cnt *= i
print(cnt)
