import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
arr.sort()
a = 0
time = [arr[0]]
for i in range(n - 1):
    time.append(arr[i+1] - arr[i])
time.sort()
for _ in range(m):
    time.pop()
print(sum(time))
