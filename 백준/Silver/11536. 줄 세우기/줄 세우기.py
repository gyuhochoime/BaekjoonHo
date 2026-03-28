import sys
n = int(sys.stdin.readline())
arr = [sys.stdin.readline().rstrip() for _ in range(n)]
increase = arr[:]
decrease = arr[:]
increase.sort()
decrease.sort(reverse = True)
if arr == increase:
    print("INCREASING")
elif arr == decrease:
    print("DECREASING")
else:
    print("NEITHER")
