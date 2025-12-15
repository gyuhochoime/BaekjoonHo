import sys
n = int(sys.stdin.readline().rstrip())
arr = []
for _ in range(n):
    a = int(sys.stdin.readline().rstrip())
    arr.append(a)
if arr[0] == 0 and arr[1] == 0:
    print(0)
else:
    if arr[1] - arr[0] == arr[2] - arr[1]:
        print(arr[-1] + (arr[1] - arr[0]))
    else:
        print(arr[-1] * (arr[1] // arr[0]))
