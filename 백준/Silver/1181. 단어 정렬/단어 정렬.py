import sys
T = int(sys.stdin.readline().rstrip())
arr = set()
for i in range(T):
    n = sys.stdin.readline().rstrip()
    arr.add(n)
aaa = list(arr)
aaa.sort()
aaa.sort(key=len)
for i in aaa:
    print(i, end = "\n")
