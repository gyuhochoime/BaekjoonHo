import sys
n = int(sys.stdin.readline())
arr = list(sys.stdin.readline().rstrip().split())
dic = dict()
for i in arr:
    dic[i] = 0
for _ in range(n):
    lst = list(sys.stdin.readline().rstrip().split())
    for i in lst:
        dic[i] += 1
student = [(key, value) for key, value in dic.items()]
student.sort(key = lambda x: (-x[1], x[0]))
for key, value in student:
    print(key, value)
