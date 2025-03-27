import sys
T = int(sys.stdin.readline().rstrip())
n = list(map(int, sys.stdin.readline().rstrip().split()))
m = list(map(int, sys.stdin.readline().rstrip().split()))

sum = 0
for i in range(T):
    if n[i] > m[i]:
        sum += n[i] - m[i]
    elif n[i] < m[i]:
        sum += m[i] - n[i]
print(sum // 2)
