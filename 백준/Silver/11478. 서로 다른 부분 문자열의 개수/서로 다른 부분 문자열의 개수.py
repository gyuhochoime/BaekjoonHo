import sys
arr = set()
a = 0
n = sys.stdin.readline().rstrip()
b = len(n)
for _ in range(len(n)):
    for j in range(len(n), 0, -1):
        arr.add(n[len(n)-j:len(n)-j+a+1])
    a += 1
print(len(arr))
