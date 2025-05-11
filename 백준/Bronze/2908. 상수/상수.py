import sys
n, m = list(map(str, sys.stdin.readline().rstrip().split()))
a = int("%s%s%s" % (n[2], n[1], n[0]))
b = int("%s%s%s" % (m[2], m[1], m[0]))
if a > b:
    print(a)
else:
    print(b)
