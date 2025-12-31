import sys
n = int(sys.stdin.readline().rstrip())
for _ in range(n):
    a = list(map(int, sys.stdin.readline().rstrip()))
    dic = dict()
    for i in a:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    print(len(dic))
