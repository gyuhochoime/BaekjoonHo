import sys
T = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
newAvg = sum(arr) / T
saejoon = newAvg / max(arr) * 100
print(saejoon)
