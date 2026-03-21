import sys
while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    dic = dict()
    for _ in range(n):
        a, b = map(str, sys.stdin.readline().split())
        dic[a] = float(b)
    arr = [(key, value) for key, value in dic.items()]
    arr.sort(key = lambda x: -x[1])
    a = arr[0][1]
    lst = []
    for key, value in arr:
        if value == a:
            lst.append(key)
    print(*lst)
