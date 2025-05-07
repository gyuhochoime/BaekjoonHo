import sys
tot = 0
for i in range(5):
    n = int(sys.stdin.readline().rstrip())
    if n <= 40:
        n = 40
    tot += n
print(tot // 5)
