import sys
n = int(sys.stdin.readline().rstrip())
prefix = [0] * 1001
prefix[1] = 1
prefix[2] = 2
for i in range(3, 1001):
    prefix[i] = prefix[i-2] + prefix[i-1]
print(prefix[n] % 10007)
