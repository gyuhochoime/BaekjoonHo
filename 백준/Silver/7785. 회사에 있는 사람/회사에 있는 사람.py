import sys
T = int(sys.stdin.readline().rstrip())
arr = []
for i in range(T):
    n, m = map(str, sys.stdin.readline().rstrip().split())
    if m == "enter":
        arr.append(n)
    elif m == "leave":
        arr.remove(n)
arr.sort(reverse = True)
for i in arr:
    print(i)
