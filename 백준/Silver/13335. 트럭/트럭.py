import sys
from collections import deque
n, w, l = map(int, sys.stdin.readline().split())
truck = list(map(int, sys.stdin.readline().split()))
truck = deque(truck)
bridge = [0] * w
bridge = deque(bridge)
time = 0
while bridge:
    time += 1
    bridge.popleft()
    if truck:
        if sum(bridge) + truck[0] <= l:
            bridge.append(truck.popleft())
        else:
            bridge.append(0)
print(time)
