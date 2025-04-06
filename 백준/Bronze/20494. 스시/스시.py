import sys
T = int(sys.stdin.readline().rstrip())
tot = 0
for i in range(T):
    susi = sys.stdin.readline().rstrip()
    tot += len(susi)
print(tot)
