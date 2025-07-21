import sys
T = int(sys.stdin.readline().rstrip())
for i in range(T):
    j, n = map(int, sys.stdin.readline().rstrip().split())
    arr = []
    tot = 0
    cnt = 0
    for i in range(n):
        r, c = map(int, sys.stdin.readline().rstrip().split())
        arr.append(r * c)
    arr.sort(reverse = True)
    for i in arr:
        tot += i
        cnt += 1
        if tot >= j:
            break
    print(cnt)
