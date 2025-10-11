import sys
n = int(sys.stdin.readline().rstrip())
arr = []
for i in range(n):
    a = int(sys.stdin.readline().rstrip())
    arr.append(a)
cnt = 0
cur = 0
while arr:
    a = arr.pop()
    if a > cur:
        cnt += 1
        cur = a
print(cnt)
