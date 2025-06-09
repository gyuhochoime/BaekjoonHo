import sys
n = int(sys.stdin.readline())
tot = 0
cnt = 0
for i in range(1, n + 1):
    tot += i
    cnt += 1
    if tot > n:
        print(cnt - 1)
        break
else:
    print(cnt)

