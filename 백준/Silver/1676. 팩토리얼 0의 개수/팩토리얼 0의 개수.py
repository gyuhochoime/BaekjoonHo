import sys
n = int(sys.stdin.readline().rstrip())
cnt = 0
tot = 1
for i in range(1, n + 1):
    tot *= i
zero = str(tot)
for i in range(len(zero), 0, -1):
    if zero[i-1] == "0":
        cnt += 1
    else:
        break
print(cnt)
