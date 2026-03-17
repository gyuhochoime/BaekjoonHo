import sys
n, m, k = map(int, sys.stdin.readline().split())
year = 1
while True:
    if (year - n) % 15 == 0 and (year - m) % 28 == 0 and (year - k) % 19 == 0:
        break
    year += 1
print(year)
