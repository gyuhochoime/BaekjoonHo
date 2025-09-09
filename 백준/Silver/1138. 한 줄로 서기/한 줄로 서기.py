import sys
n = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
order = [0] * n
for i in range(n):
    for j in range(n):
        if arr[i] == 0 and order[j] == 0:
            order[j] = i + 1
            break
        elif order[j] == 0:
            arr[i] -= 1
for i in order:
    print(i, end = " ")
