import sys
n = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
cps = []
joong = set(arr)
joong = list(joong)
joong.sort()
soon = dict()
for i in range(len(joong)):
    soon[joong[i]] = i
for i in arr:
    cps.append(soon[i])
print(*cps)
