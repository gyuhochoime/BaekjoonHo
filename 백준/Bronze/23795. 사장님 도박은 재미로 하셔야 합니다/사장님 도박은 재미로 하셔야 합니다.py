import sys
tot = 0
while True:
    n = int(sys.stdin.readline().rstrip())
    if n == -1:
        break
    tot += n
print(tot)
