import sys
T = int(sys.stdin.readline().rstrip())
arr = []
for i in range(T):
    n = int(sys.stdin.readline().rstrip())
    arr.append(n)
arr.sort()
tot = 0
for i in range(1, T + 1):
    tot += abs(arr[i-1] - i)
print(tot)
