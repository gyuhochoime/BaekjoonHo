import sys
T = int(sys.stdin.readline().rstrip())
a, b = map(int, sys.stdin.readline().rstrip().split())
c = int(sys.stdin.readline().rstrip())
tot = c
dang = a
cal = c // a
arr = []
for i in range(T):
    n = int(sys.stdin.readline().rstrip())
    arr.append(n)
arr.sort(reverse = True)
for i in arr:
    tot += i
    dang += b
    if tot // dang >= cal:
        cal = tot // dang
    else:
        break
print(cal)
