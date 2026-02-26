import sys
import heapq
n = int(sys.stdin.readline())
heap = []
for _ in range(n):
    a = int(sys.stdin.readline())
    if a != 0:
        heapq.heappush(heap, (abs(a), a))
    else:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)
