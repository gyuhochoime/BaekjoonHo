import sys
import math
T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    n = int(sys.stdin.readline().rstrip())
    if n == 0 or n == 1:
        print(2)
    else:
        while True:
            for i in range(2, int(math.sqrt(n) + 1)):
                if n % i == 0:
                    break
            else:
                print(n)
                break
            n += 1
