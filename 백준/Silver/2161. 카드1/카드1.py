import sys
from collections import deque
n = int(sys.stdin.readline().rstrip())
card = [i for i in range(1, n + 1)]
card = deque(card)
seq = []
while card:
    if len(card) > 1:
        seq.append(card.popleft())
        card.append(card.popleft())
    else:
        seq.append(card.popleft())
for i in seq:
    print(i, end = " ")
