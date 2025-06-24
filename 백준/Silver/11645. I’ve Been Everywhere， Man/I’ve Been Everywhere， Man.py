import sys
T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    n = int(sys.stdin.readline().rstrip())
    arr = []
    for _ in range(n):
        m = sys.stdin.readline().rstrip()
        arr.append(m)
    arr = set(arr)
    print(len(arr))
