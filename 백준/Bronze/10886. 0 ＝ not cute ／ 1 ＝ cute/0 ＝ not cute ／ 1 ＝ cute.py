import sys
n = int(sys.stdin.readline().rstrip())
arr = dict()
for _ in range(n):
    a = int(sys.stdin.readline().rstrip())
    if a not in arr:
        arr[a] = 1
    else:
        arr[a] += 1
cute = [(key, value) for key, value in arr.items()]
cute.sort(key = lambda x: (-x[1]))
if cute[0][0] == 0:
    print("Junhee is not cute!")
else:
    print("Junhee is cute!")
