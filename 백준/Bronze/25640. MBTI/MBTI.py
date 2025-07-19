import sys
n = sys.stdin.readline().rstrip()                                              
T = int(sys.stdin.readline().rstrip())
arr = []
cnt = 0
for i in range(T):
    a = sys.stdin.readline().rstrip()
    arr.append(a)
for i in arr:
    if i == n:
        cnt += 1
print(cnt)
