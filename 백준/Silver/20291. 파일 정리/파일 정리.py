import sys
n = int(sys.stdin.readline().rstrip())
arr = dict()
exp = []
for _ in range(n):
    a = sys.stdin.readline().rstrip()
    for i in range(len(a)):
        if a[i] == ".":
            if a[i+1:] in arr:
                arr[a[i+1:]] += 1
            else:
                arr[a[i+1:]] = 1
for key, val in arr.items():
    exp.append((key, val))
exp.sort(key = lambda x: (x[0]))
for key, val in exp:
    print(key, val)
