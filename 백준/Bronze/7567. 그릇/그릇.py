import sys
n = list(map(str, sys.stdin.readline().rstrip()))
tot = 10
for i in range(1, len(n)):
    if n[i] != n[i-1]:
        tot += 10
    else:
        tot += 5
print(tot)
