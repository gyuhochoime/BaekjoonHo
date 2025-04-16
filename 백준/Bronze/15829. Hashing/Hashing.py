import sys
n = int(sys.stdin.readline().rstrip())
m = list(sys.stdin.readline().rstrip())
mod = 1234567891
tot = 0
for i in range(n):
    tot += (ord(m[i])-96) * 31 ** i
print(tot % mod)
