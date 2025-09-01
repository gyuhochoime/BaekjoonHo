import sys
n = list(sys.stdin.readline().rstrip())
arr = list(sys.stdin.readline().rstrip())
while len(arr) != len(n):
    if arr[len(arr)-1] == "A":
        arr.pop()
    elif arr[len(arr)-1] == "B":
        arr.pop()
        arr.reverse()
if n == arr:
    print(1)
else:
    print(0)
    
