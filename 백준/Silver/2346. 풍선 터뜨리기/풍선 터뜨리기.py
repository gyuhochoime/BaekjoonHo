import sys
from collections import deque
n = int(sys.stdin.readline().rstrip())
balloon = list(map(int, sys.stdin.readline().rstrip().split()))
order = [x for x in range(1, n + 1)]
seq = []
balloon, order = deque(balloon), deque(order)
while balloon:
    a = balloon.popleft()
    seq.append(order.popleft())
    if balloon and a > 0:
        for _ in range(a - 1):
            balloon.append(balloon.popleft())
            order.append(order.popleft())
    elif balloon and a < 0:
        for _ in range(abs(a)):
            balloon.appendleft(balloon.pop())
            order.appendleft(order.pop())
print(*seq)
