import sys
T = int(sys.stdin.readline())

for _ in range(T):
    h, w, n = map(int, sys.stdin.readline().split())

    floor = n % h
    room = n // h + 1

    if floor == 0:
        floor = h
        room = n // h

    print(f"{floor}{room:02d}")
