import sys
n = int(sys.stdin.readline().rstrip())
tile = [0] * 1001
tile[0], tile[1] = 1, 3
for i in range(2, 1000):
    tile[i] = tile[i-1] + tile[i-2] * 2
print(tile[n-1] % 10007)
