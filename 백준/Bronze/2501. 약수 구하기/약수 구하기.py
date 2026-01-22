import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
sosu = []
for i in range(1, n + 1):
    if n % i == 0:
        sosu.append(i)
if m > len(sosu):
    print(0)
else:
    print(sosu[m-1])
