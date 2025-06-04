import sys
arr = []
for i in range(5):
    n = int(sys.stdin.readline().rstrip())
    arr.append(n)
arr.sort()
print(sum(arr) // 5)
print(arr[2])
