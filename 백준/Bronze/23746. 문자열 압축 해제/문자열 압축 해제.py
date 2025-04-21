import sys
T = int(sys.stdin.readline().rstrip())
arr = [] * 5
brr = [] * 5
a = ""
for i in range(T):
    n, m = sys.stdin.readline().rstrip().split()
    arr.append(n)
    brr.append(m)
k = list(sys.stdin.readline().rstrip())
for i in range(len(k)):
    for j in range(T):
        if k[i] == brr[j]:
            k[i] = arr[j]
for i in range(len(k)):
    a += k[i]
fidx, lidx = map(int, sys.stdin.readline().rstrip().split())
print(a[fidx - 1:lidx])
