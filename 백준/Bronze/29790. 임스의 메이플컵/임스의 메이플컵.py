import sys
n, m, r = map(int, sys.stdin.readline().split())

if n >= 1000 and (m >= 8000 or r >= 260):
    print("Very Good")
elif n >= 1000:
    print("Good")
else:
    print("Bad")