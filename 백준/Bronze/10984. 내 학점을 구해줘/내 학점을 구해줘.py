import sys
n = int(sys.stdin.readline().rstrip())
for _ in range(n):
    chong = 0
    hak = 0
    m = int(sys.stdin.readline().rstrip())
    for _ in range(m):
        a, b = map(float, sys.stdin.readline().rstrip().split())
        chong += int(a)
        hak += a * b
    gpa = hak / chong
    print(chong, round(gpa, 1))
