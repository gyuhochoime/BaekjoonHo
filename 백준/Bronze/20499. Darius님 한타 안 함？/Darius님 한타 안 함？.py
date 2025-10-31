import sys
n, m, k = map(int, sys.stdin.readline().rstrip().split("/"))
if n + k < m or m == 0:
    print("hasu")
else:
    print("gosu")
