import sys
T = int(sys.stdin.readline().rstrip())
cnt = T // 3
arr = []
for i in range(T):
    n = int(sys.stdin.readline().rstrip())
    arr.append(n)
arr.sort(reverse = True)
for i in range(cnt):
    arr.pop(2 + 2 * i)
print(sum(arr))
