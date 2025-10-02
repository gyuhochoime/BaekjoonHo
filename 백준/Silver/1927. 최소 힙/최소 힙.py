import sys
import heapq as hq
n = int(sys.stdin.readline().rstrip())
arr = []
for i in range(n):
    a = int(sys.stdin.readline().rstrip())
    if a == 0 and len(arr) == 0:
        print(0)
    elif a == 0:
        print(hq.heappop(arr))
    else:
        hq.heappush(arr, a)
