import sys
n = list(sys.stdin.readline().rstrip())
cam = ["A", "B", "C", "D", "E", "G", "I", "M", "R"]
arr = []
for i in n:
    if i not in cam:
        arr.append(i)
for i in arr:
    print(i, end = "")
        
