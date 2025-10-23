import sys
n = sys.stdin.readline().rstrip()
cnt = 0
arr = []
for i in n:
    if i == "(":
        arr.append(i)
    else:
        if len(arr) == 0:
            cnt += 1
        else:
            arr.pop()
while arr:
    arr.pop()
    cnt += 1
print(cnt)
