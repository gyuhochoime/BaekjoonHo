import sys
n = int(sys.stdin.readline().rstrip())
for i in range(n):
    a = int(sys.stdin.readline().rstrip())
    if (a + 1) % (a % 100) == 0:
        print("Good")
    else:
        print("Bye")
