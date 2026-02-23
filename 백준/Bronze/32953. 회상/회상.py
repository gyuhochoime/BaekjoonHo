import sys
n, m = map(int, sys.stdin.readline().split())
dic = dict()
cnt = 0
for _ in range(n):
    a = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    for i in arr:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
stu = [(key, value) for key, value in dic.items()]
for key, value in stu:
    if value >= m:
        cnt += 1
print(cnt)
