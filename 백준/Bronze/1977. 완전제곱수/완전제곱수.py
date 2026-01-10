import sys
jae = [0] * 10001
tot = 0
fir = 10001
for i in range(1, 101):
    jae[i**2] = 1
n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())
for i in range(n, m + 1):
    if jae[i] == 1:
        tot += i
        fir = min(fir, i)
if tot == 0:
    print(-1)
else:
    print(tot)
    print(fir)
