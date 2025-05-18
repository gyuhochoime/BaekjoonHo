import sys
T = int(sys.stdin.readline().rstrip())
arr = []
for i in range(T):
    n = int(sys.stdin.readline().rstrip())
    if n == 0:
        arr.pop()
    else:
        arr.append(n)
print(sum(arr))
