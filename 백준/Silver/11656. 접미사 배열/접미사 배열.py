import sys
arr = sys.stdin.readline().rstrip()
tail = []
for i in range(len(arr)):
    tail.append(arr)
    arr = arr[1:]
tail.sort()
for i in tail:
    print(i)
