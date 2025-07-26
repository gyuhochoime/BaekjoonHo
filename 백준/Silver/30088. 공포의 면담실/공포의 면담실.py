import sys
n = int(sys.stdin.readline().rstrip())
arm = []
tot = 0
time = 0
for i in range(n):
    arr = list(map(int, sys.stdin.readline().rstrip().split()))
    arm.append(sum(arr) - arr[0])
arm.sort()
for i in arm:
    time += i
    tot += time
print(tot)
