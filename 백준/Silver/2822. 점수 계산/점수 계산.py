import sys
arr = []
arm = []
for i in range(1, 9):
    n = int(sys.stdin.readline().rstrip())
    arr.append(n)
score = list(arr)
arr.sort(reverse = True)
tot = 0
for i in range(5):
    tot += arr[i]
    arm.append(score.index(arr[i]) + 1)
arm.sort()
print(tot)
for i in arm:
    print(i, end = " ")
