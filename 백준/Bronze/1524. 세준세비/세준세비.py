import sys
T = int(sys.stdin.readline().rstrip())
for i in range(T):
    a = sys.stdin.readline().rstrip()
    n, m = map(int, sys.stdin.readline().rstrip().split())
    june = list(map(int, sys.stdin.readline().rstrip().split()))
    bee = list(map(int, sys.stdin.readline().rstrip().split()))
    june.sort(reverse = True)
    bee.sort(reverse = True)
    if june[0] >= bee[0]:
        print("S")
    else:
        print("B")
    
