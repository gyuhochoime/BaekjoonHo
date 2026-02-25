import sys
import heapq
n = int(sys.stdin.readline())
arr = (list(map(int, sys.stdin.readline().split())))
heapq.heapify(arr)
for _ in range(n - 1):
    a = list(map(int, sys.stdin.readline().split()))
    for i in a:
        if i > arr[0]:
            heapq.heappop(arr)
            heapq.heappush(arr, i)
print(arr[0])
