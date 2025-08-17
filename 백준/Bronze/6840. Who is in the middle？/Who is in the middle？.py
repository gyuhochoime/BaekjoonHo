import sys
arr = []
for i in range(3):
    n = int(sys.stdin.readline().rstrip())
    arr.append(n)
arr.sort()
print(arr[1])
