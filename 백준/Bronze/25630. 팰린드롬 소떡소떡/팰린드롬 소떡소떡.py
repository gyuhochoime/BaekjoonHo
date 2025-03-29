import sys

n = int(sys.stdin.readline().rstrip())
m = list(sys.stdin.readline().rstrip())
tot = 0
for i in range(n // 2):
    if m[i] != m[n-i-1]:
        m[i] = m[n-i-1]
        tot += 1
print(tot)
