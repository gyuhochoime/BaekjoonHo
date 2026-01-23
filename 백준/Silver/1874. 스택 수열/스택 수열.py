import sys
n = int(sys.stdin.readline().rstrip())
stack = []
tmp = []
cnt = 1
temp = True
for i in range(n):
    a = int(sys.stdin.readline().rstrip())
    while cnt <= a:
        stack.append(cnt)
        tmp.append("+")
        cnt += 1
    if stack[-1] == a:
        stack.pop()
        tmp.append("-")
    else:
        temp = False
        break
if temp == False:
    print("NO")
else:
    for i in tmp:
        print(i)
