import sys
n = int(sys.stdin.readline())
nine = ""
while n > 0:
    nine = str(n % 9) + nine
    n //= 9
print(nine)
