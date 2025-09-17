import sys
T = int(sys.stdin.readline().rstrip())
dic = {}
for i in range(T):
    n = sys.stdin.readline().rstrip()
    if n in dic:
        dic[n] += 1
    else:
        dic[n] = 1
sorted_dic = sorted(dic.items(), key = lambda x: (-x[1], x[0]))
print(sorted_dic[0][0])
