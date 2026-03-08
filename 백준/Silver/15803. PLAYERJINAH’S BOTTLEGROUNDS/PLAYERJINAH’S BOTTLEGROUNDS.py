import sys
arr = []
for _ in range(3):
    a, b = map(int, sys.stdin.readline().split())
    arr.append((a, b))
if (arr[1][0] - arr[0][0]) * (arr[2][1] - arr[0][1]) == (arr[1][1] - arr[0][1]) * (arr[2][0] - arr[0][0]):
    print("WHERE IS MY CHICKEN?")
else:
    print("WINNER WINNER CHICKEN DINNER!")
