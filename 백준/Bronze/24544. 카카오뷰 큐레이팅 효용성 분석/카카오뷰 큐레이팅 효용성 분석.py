import sys
T = int(sys.stdin.readline().rstrip())
interesting = list(map(int, sys.stdin.readline().rstrip().split()))
myView = list(map(int, sys.stdin.readline().rstrip().split()))
tot = 0
emion = 0
for i in range(T):
    tot += interesting[i]
    if myView[i] == 1:
        emion += interesting[i]
print(tot)
print(tot - emion)
