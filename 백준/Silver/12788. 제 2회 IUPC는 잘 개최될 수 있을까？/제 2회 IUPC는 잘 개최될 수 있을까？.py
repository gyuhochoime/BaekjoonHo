import sys
n = int(sys.stdin.readline().rstrip())
m, k = map(int, sys.stdin.readline().rstrip().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
arr.sort(reverse = True)
person = m * k
tot = 0
cnt = 0
for i in arr:
    if tot < person:
        tot += i
        cnt += 1
    else:
        break
if tot < person:
    print("STRESS")
else:
    print(cnt)
