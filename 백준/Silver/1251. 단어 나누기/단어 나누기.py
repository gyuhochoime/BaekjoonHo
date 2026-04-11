import sys
n = sys.stdin.readline().rstrip()
arr = []
for i in range(1, len(n)):
    for j in range(i + 1, len(n)):
        a = n[:i][::-1]
        b = n[i:j][::-1]
        c = n[j:][::-1]
        arr.append(a + b + c)
arr.sort()
print(arr[0])