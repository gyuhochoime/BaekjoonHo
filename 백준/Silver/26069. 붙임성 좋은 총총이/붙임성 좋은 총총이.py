import sys
n = int(sys.stdin.readline())
rbd = []
for _ in range(n):
    a, b = map(str, sys.stdin.readline().split())
    if a == "ChongChong" or b == "ChongChong":
        rbd.append(a)
        rbd.append(b)
    if a in rbd or b in rbd:
        rbd.append(a)
        rbd.append(b)
rbd = set(rbd)
print(len(rbd))
