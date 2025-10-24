import sys
n = int(sys.stdin.readline().rstrip())
frt = list(map(int, sys.stdin.readline().rstrip().split()))
grt = list(map(int, sys.stdin.readline().rstrip().split()))
arr = []
for i in range(n):
    arr.append((frt[i], grt[i]))
arr.sort(key = lambda x: (x[1], x[0]))
tot = 0
cnt = 0
for key, value in arr:
    tot += key + value * cnt
    cnt += 1
print(tot)
