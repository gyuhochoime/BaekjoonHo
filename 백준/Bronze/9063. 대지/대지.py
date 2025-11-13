import sys
n = int(sys.stdin.readline().rstrip())
garo = 0
sero = 0
ara = []
arb = []
for _ in range(n):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    ara.append(a)
    arb.append(b)
garo = max(ara) - min(ara)
sero = max(arb) - min(arb)
print(garo * sero)
