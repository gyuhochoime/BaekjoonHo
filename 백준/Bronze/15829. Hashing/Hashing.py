import sys
n = int(sys.stdin.readline().rstrip())
m = list(sys.stdin.readline().rstrip())
tot = 0
for i in range(n):
    tot += (ord(m[i])-96) * 31 ** i
print(tot)
