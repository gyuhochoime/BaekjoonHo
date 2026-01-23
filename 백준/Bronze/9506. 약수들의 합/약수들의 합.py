import sys
while True:
    n = int(sys.stdin.readline().rstrip())
    if n == -1:
        break
    measure = []
    for i in range(1, n):
        if n % i == 0:
            measure.append(i)
    if sum(measure) == n:
        print(n, "=", end = " ")
        print(*measure, sep = " + ")
    else:
        print("%d is NOT perfect." % n)
