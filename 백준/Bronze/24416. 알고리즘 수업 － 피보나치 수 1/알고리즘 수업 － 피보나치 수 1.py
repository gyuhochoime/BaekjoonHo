import sys
n = int(sys.stdin.readline())
prefix = [0] * 41
prefix[3], prefix[4] = 2, 3
for i in range(5, 41):
    prefix[i] = prefix[i-1] + prefix[i-2]
print(prefix[n], n - 2)
