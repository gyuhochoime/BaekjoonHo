import sys
T = int(sys.stdin.readline().rstrip())
arr = []
for i in range(T):
    price = int(sys.stdin.readline().rstrip())
    arr.append(price)
n = int(sys.stdin.readline().rstrip())
tot = 0
for i in range(n):
    want = int(sys.stdin.readline().rstrip())
    tot += arr[want-1]
print(tot)
