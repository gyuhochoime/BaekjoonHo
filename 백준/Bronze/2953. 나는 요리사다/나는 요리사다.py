import sys
arr = dict()
for i in range(1, 6):
    a = list(map(int, sys.stdin.readline().rstrip().split()))
    arr[i] = sum(a)
winner = [(key, value) for key, value in arr.items()]
winner.sort(key = lambda x: (-x[1]))
print(winner[0][0], winner[0][1])
