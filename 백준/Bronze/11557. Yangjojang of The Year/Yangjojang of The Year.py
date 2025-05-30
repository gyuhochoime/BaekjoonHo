import sys
T = int(sys.stdin.readline().rstrip())
for i in range(T):
    N = int(sys.stdin.readline().rstrip())
    arr = []
    for i in range(N):    
        n, m = map(str, sys.stdin.readline().rstrip().split())
        arr.append([n, int(m)])
    arr.sort(key = lambda x: x[1], reverse = True)
    print(arr[0][0])
