import sys
T = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
park = 0
sung = 0
arr.sort()
for i in range(T // 2):
    park += arr[i]
for i in range(T // 2, T):
    sung += arr[i]
print(park, sung)
