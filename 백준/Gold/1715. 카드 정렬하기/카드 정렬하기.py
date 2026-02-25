import sys
import heapq
n = int(sys.stdin.readline())
card = [int(sys.stdin.readline()) for _ in range(n)]
heapq.heapify(card)
tot = 0
if n == 1:
    print(0)
else:
    while len(card) > 1:
        a = heapq.heappop(card)
        b = heapq.heappop(card)
        tot += a + b
        heapq.heappush(card, a + b)
    print(tot)
