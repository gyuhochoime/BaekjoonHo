import sys
T = int(sys.stdin.readline().rstrip())
time = []
for i in range(T):
    s, e = map(int, sys.stdin.readline().rstrip().split())
    time.append((s, e))
time.sort(key = lambda x: (x[1], x[0]))
endTime = 0
cnt = 0
for s, e in time:
    if s >= endTime:
        endTime = e
        cnt += 1
print(cnt)
