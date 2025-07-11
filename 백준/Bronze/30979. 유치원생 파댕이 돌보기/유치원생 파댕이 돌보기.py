import sys
T = int(sys.stdin.readline().rstrip())
n = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
if sum(arr) >= T:
    print("Padaeng_i Happy")
else:
    print("Padaeng_i Cry")
