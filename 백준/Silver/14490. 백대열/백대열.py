import sys

def get_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

n, m = map(int, sys.stdin.readline().rstrip().split(":"))
gcd = get_gcd(n, m)
print(f"{n // gcd}:{m // gcd}")
