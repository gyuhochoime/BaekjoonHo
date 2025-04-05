import sys
n = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
tot = 0
for i in range(3):
    if n >= arr[i]:
        tot += arr[i]
    elif n < arr[i]:
        tot += n
print(tot)
