import sys
n = list(sys.stdin.readline().rstrip())
tot = 0
for i in range(len(n)):
    tot += int(n[i])**5
print(tot)
