import sys
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
stack = []
top = [0] * n
for i in range(n):
    while stack:
        if stack[-1][0] > arr[i]:
            top[i] = stack[-1][1] + 1
            break
        else:
            stack.pop()
    stack.append((arr[i], i))
print(*top)
