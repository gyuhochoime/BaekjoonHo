import sys
n, m, k = map(int, sys.stdin.readline().rstrip().split())
mock = k // m
namuji = k % m
print(mock, namuji)
