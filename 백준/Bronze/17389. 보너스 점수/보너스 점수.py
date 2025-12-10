import sys
n = int(sys.stdin.readline().rstrip())
arr = list(sys.stdin.readline().rstrip())
cnt = 0
bonus = 0
tot = 0
for i in arr:
    cnt += 1
    if i == "O":
        tot += cnt
        tot += bonus
        bonus += 1
    else:
        bonus = 0
print(tot)
