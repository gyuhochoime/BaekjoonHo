import sys
import heapq
n = int(sys.stdin.readline())
lec = []
room = []
for _ in range(n):
    s, e = map(int, sys.stdin.readline().split())
    lec.append((s, e))
lec.sort()
heapq.heappush(room, lec[0][1])
for i in range(1, n):
    if lec[i][0] < room[0]:
        heapq.heappush(room, lec[i][1])
    else:
        heapq.heappop(room)
        heapq.heappush(room, lec[i][1])
print(len(room))
