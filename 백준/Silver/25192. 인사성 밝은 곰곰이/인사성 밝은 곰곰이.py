import sys
n = int(sys.stdin.readline().rstrip())
arr = set()
cnt = 0
for i in range(n):
    n = sys.stdin.readline().rstrip()
    if n == "ENTER":
        arr.clear()
    elif n not in arr:
        cnt += 1
        arr.add(n)
print(cnt)
