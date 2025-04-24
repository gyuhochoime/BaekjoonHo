import sys
n = list(map(int, sys.stdin.readline().rstrip()))
m = list(map(int, sys.stdin.readline().rstrip()))
arr = []
for i in range(8):
    arr.append(n[i])
    arr.append(m[i])
gone = arr
while len(gone) > 2:
    tmp = []
    for i in range(len(gone) - 1):
        tmp.append((gone[i] + gone[i + 1]) % 10)
    gone = tmp
print(str(gone[0]) + str(gone[1]))
