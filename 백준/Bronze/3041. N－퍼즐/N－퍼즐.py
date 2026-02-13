import sys
puzzle = [list(map(str, sys.stdin.readline())) for _ in range(4)]
dot = 0
for i in range(4):
    for j in range(4):
        if puzzle[i][j] != ".":
            n = ord(puzzle[i][j]) - ord("A")
            a = n // 4
            b = n % 4
            dot += abs(i - a) + abs(j - b)
print(dot)
