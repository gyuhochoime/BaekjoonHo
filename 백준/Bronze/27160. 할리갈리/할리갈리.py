import sys
n = int(sys.stdin.readline().rstrip())
dic = dict()
for _ in range(n):
    a, b = map(str, sys.stdin.readline().rstrip().split())
    if a in dic:
        dic[a] += int(b)
    else:
        dic[a] = int(b)
hal = [(key, value) for key, value in dic.items()]
for fru, num in hal:
    if num == 5:
        print("YES")
        break
else:
    print("NO")
