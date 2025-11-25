import sys
n = int(sys.stdin.readline().rstrip())
for _ in range(n):
    a = list(map(str, sys.stdin.readline().rstrip().split()))
    a[0] = "god"
    for i in a:
        print(i, end = "")
    print()
