import sys
n = sys.stdin.readline().rstrip()
tot = 0
i = 0
a = len(n)
b = 1
c = int(n)
while a > 1:
    tot += 9 * b * 10 ** i
    a -= 1
    b += 1
    i += 1
c -= 10 ** i - 1
tot += c * b
print(tot)
