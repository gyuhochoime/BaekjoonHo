import sys

arr = []
for i in range(1, 6):
    n = sys.stdin.readline().rstrip()
    if "FBI" in n:
        arr.append(i)
if arr == []:
    print("HE GOT AWAY!")
else:
    print(*arr)
