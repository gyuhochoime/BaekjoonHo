import sys
T = int(sys.stdin.readline())
for i in range(1, T + 1):
    arr = list(map(int, sys.stdin.readline().split()))
    arr.pop(0)
    arr.sort()
    lg = []
    for j in range(len(arr) - 1):
        lg.append(arr[j+1] - arr[j])
    a = max(lg)
    print("Class %d" % i)
    print("Max %d, Min %d, Largest gap %d" % (arr[-1], arr[0], a))
