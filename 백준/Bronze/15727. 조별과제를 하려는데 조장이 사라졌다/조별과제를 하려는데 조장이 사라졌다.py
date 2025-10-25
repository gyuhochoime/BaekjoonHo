import sys
n = int(sys.stdin.readline().rstrip())
cnt = 0
cnt += n // 5
a = n % 5
if a != 0:
    cnt += 1
print(cnt)
