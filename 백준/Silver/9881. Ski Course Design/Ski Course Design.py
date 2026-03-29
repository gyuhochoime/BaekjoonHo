import sys
n = int(sys.stdin.readline())
arr = []
for _ in range(n):
    a = int(sys.stdin.readline())
    arr.append(a)
high = max(arr)
low = min(arr)
if high - low <= 17:
    print(0)
else:
    tot = 2100000000
    for i in range(84):
        rt = i + 17
        cost = 0
        for j in arr:
            if j < i:
                cost += (i - j) ** 2
            elif j > rt:
                cost += (j - rt) ** 2
        if cost < tot:
            tot = cost
    print(tot)
