import sys
tot = 0
lst = 100
for i in range(7):
    n = int(sys.stdin.readline().rstrip())
    if n % 2 == 1:
        tot += n
        lst = min(n, lst)
if tot == 0:
    print(-1)
else:
    print(tot)
    print(lst)