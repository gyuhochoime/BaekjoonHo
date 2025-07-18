import sys
T = int(sys.stdin.readline().rstrip())
arr = []
for i in range(T):
    n = int(sys.stdin.readline().rstrip())
    arr.append(n)
if arr[0] == max(arr):
    print("hard")
elif arr[0] == min(arr):
    print("ez")
else:
    print("?")
