import sys
import heapq as hq
n = int(sys.stdin.readline().rstrip())
arr = []
for _ in range(n):
    a = list(map(int, sys.stdin.readline().rstrip().split()))
    if a[0] != 0:
        a.pop(0)
        for i in a:
            hq.heappush(arr, -i)
    else:
        if len(arr) == 0:
            print(-1)
        else:
            print(-hq.heappop(arr))
