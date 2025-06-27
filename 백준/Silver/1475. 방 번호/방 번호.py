import sys
arr = list(map(int, sys.stdin.readline().rstrip()))
tot = [0] * 10
for i in arr:
    if i == 6 or i == 9:
        tot[6] += 1
    else:
        tot[i] += 1
if tot[6] % 2 == 0:
    tot[6] = tot[6] // 2
elif tot[6] % 2 == 1:
    tot[6] = tot[6] // 2 + 1
print(max(tot))
