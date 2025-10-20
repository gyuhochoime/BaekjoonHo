import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
arn = list(map(int, sys.stdin.readline().rstrip().split()))
arm = list(map(int, sys.stdin.readline().rstrip().split()))
cha = dict()
chacha = []
for i in arn:
    cha[i] = 1
for i in arm:
    if i in cha:
        cha[i] = 0
for key, value in cha.items():
    if value == 1:
        chacha.append((key, value))
chacha.sort()
if len(chacha) == 0:
    print(0)
else:
    print(len(chacha))
    for key, value in chacha:
        print(key, end = " ")
