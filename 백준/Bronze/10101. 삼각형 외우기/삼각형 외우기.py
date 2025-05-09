import sys
n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())
k = int(sys.stdin.readline().rstrip())
if n + m + k != 180:
    print("Error")
elif n + m + k == 180 and n != m and m != k and k != n:
    print("Scalene")
elif n == 60 and m == 60 and k == 60:
    print("Equilateral")
else:
    print("Isosceles")
