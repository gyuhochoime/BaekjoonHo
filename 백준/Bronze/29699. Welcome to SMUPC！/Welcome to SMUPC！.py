import sys
a = ["W", "e", "l", "c", "o", "m", "e", "T", "o", "S", "M", "U", "P", "C"]
n = int(sys.stdin.readline().rstrip())
m = n % 14
print(a[m-1])
