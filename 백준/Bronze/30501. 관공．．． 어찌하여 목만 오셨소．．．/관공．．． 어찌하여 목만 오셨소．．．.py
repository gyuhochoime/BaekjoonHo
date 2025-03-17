import sys

n = int(sys.stdin.readline().rstrip())
arr = []
for i in range(n):
    name = sys.stdin.readline().rstrip()
    for j in range(len(name)):
        if name[j] == "S":
            arr.append(name)
print(arr[0])
