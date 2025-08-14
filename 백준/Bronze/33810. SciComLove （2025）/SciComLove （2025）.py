import sys
arr = ["S", "c", "i", "C", "o", "m", "L", "o", "v", "e"]
a = list(map(str, sys.stdin.readline().rstrip()))
cnt = 0
for i in range(10):
    if arr[i] != a[i]:
        cnt += 1
print(cnt)
