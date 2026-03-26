import sys
n, m = map(int, sys.stdin.readline().split())
a = 0
i = 1
jarisu = 9
while m > i * jarisu:
    m -= i * jarisu
    a += jarisu
    jarisu *= 10
    i += 1
real_num = a + 1 + (m - 1) // i
if real_num > n:
    print(-1)
else:
    print(str(real_num)[(m-1)%i])
