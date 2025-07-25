import sys
T = int(sys.stdin.readline().rstrip())
for i in range(T):
    n = int(sys.stdin.readline().rstrip())
    arr= list(map(int, sys.stdin.readline().rstrip().split()))
    arr.sort(reverse = True)
    tot = 0
    for i in range(2, n, 3):
        tot += arr[i]
    print(tot)
