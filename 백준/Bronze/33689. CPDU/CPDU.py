import sys
T = int(sys.stdin.readline().rstrip())
arr = []
cnt = 0
for i in range(T):
    n = list(sys.stdin.readline().rstrip())
    if n[0] == "C":
        cnt += 1
print(cnt)
