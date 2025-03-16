import sys

arr = [0] * 42
k = set()
for i in range(10):
    a = int(sys.stdin.readline().rstrip())
    m = a % 42 - 1
    arr[m] += 1
    if arr[m] != 0:
        k.add(m)
print(len(k))
