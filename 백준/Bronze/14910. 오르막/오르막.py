import sys
arr = list(map(int, sys.stdin.readline().rstrip().split()))
a = arr.copy()
a.sort()
if arr == a:
    print("Good")
else:
    print("Bad")
