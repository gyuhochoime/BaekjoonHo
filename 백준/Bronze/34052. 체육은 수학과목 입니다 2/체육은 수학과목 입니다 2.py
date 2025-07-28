import sys
arr = []
for i in range(4):
    n = int(sys.stdin.readline().rstrip())
    arr.append(n)
if sum(arr) <= 1500:
    print("Yes")
else:
    print("No")
