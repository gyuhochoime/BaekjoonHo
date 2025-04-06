import sys
n = list(sys.stdin.readline().rstrip())
T = int(sys.stdin.readline().rstrip())
for i in range(T):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    tmp = n[a]
    n[a] = n[b]
    n[b] = tmp
for i in range(len(n)):
    print(n[i], end = "")
        
