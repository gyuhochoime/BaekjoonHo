import sys
T = int(sys.stdin.readline().rstrip())
arr = []
for i in range(T):
    n = sys.stdin.readline().rstrip()
    n = n.lower()
    arr.append(n)
for i in arr:
    print(i)
