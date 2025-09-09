import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
arr = []
for i in range(m):
    k, r = map(int, sys.stdin.readline().rstrip().split())
    arr.append((k, r))
arr.sort(key = lambda x: (x[0]))
tot = 0
ssa = arr[0][0]
arr.sort(key = lambda x: (x[1]))
if (n // 6) * ssa < arr[0][1] * 6 * (n // 6):
    tot += (n // 6) * ssa
else:
    tot += arr[0][1] * 6 * (n // 6)
a = n % 6
if a * arr[0][1] >= ssa:
    tot += ssa
else:
    tot += a * arr[0][1]
print(tot)
