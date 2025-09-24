import sys
T = int(sys.stdin.readline().rstrip())
arr = set()
for i in range(T):
    a = list(sys.stdin.readline().rstrip())
    a.sort()
    m = ""
    for j in a:
        m += j
    arr.add(m)
print(len(arr))
