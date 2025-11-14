import sys
n = int(sys.stdin.readline().rstrip())
for i in range(n):
    arr = list(map(str, sys.stdin.readline().rstrip()))
    arr[0] = arr[0].upper()
    for x in arr:
        print(x, end = "")
    print()
