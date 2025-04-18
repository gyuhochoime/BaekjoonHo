import sys
T = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
tot = 0
for i in range(T):
    if arr[i] == 1:
        continue
    for j in range(2, arr[i] // 2 + 1):
        if arr[i] % j == 0:
            break
    else:
        tot += 1
print(tot)
