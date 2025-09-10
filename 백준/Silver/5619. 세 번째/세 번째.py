import sys
T = int(sys.stdin.readline().rstrip())
arr = []
arn = []
for _ in range(T):
    a = sys.stdin.readline().rstrip()
    arr.append(a)
for i in range(T):
    for j in range(T):
        if i == j:
            continue
        else:
            arn.append(int(arr[i] + arr[j]))
            if len(arn) > 3:
                arn.sort()
                arn.pop()
arn.sort()
print(arn[2])
