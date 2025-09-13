import sys
T = int(sys.stdin.readline().rstrip())
for i in range(T):
    y = 0
    k = 0
    for _ in range(9):
        n, m = map(int, sys.stdin.readline().rstrip().split())
        y += n
        k += m
    if y > k:
        print("Yonsei")
    elif y == k:
        print("Draw")
    elif y < k:
        print("Korea")
