import sys
n = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
a, b = map(int, sys.stdin.readline().rstrip().split())
tot = 0
for i in range(len(arr)):
    tot += arr[i] // a + 1
    if arr[i] % a == 0:
        tot -= 1
print(tot)
print(n // b, n % b)
