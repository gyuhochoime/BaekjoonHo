import sys
necessary = []
optional = []
for i in range(4):
    n = int(sys.stdin.readline().rstrip())
    necessary.append(n)
for i in range(2):
    n = int(sys.stdin.readline().rstrip())
    optional.append(n)
necessary.sort(reverse = True)
optional.sort(reverse = True)
cnt = 0
cnt += sum(necessary[:3])
cnt += sum(optional[:1])
print(cnt)
