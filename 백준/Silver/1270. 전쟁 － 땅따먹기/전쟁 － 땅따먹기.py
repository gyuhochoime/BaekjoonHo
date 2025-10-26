import sys
n = int(sys.stdin.readline().rstrip())
for _ in range(n):
    a = dict()
    arr = list(map(int, sys.stdin.readline().rstrip().split()))
    war = []
    for i in range(1, arr[0] + 1):
        if arr[i] not in a:
            a[arr[i]] = 1
        else:
            a[arr[i]] += 1
    for key, val in a.items():
        war.append((key, val))
    war.sort(key = lambda x: (-x[1]))
    if arr[0] // 2 < war[0][1]:
        print(war[0][0])
    else:
        print("SYJKGW")
