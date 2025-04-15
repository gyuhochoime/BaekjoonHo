import sys
arr = [-1] * 26
n = list(sys.stdin.readline().rstrip())
for i in range(len(n)):
    if arr[ord(n[i])-97] == -1:
        arr[ord(n[i])-97] = i
for i in arr:
    print(i, end = " ")
