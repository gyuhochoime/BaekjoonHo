import sys

n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())
k = int(sys.stdin.readline().rstrip())
i = int(sys.stdin.readline().rstrip())
total = n + m + k + i
mok = total // 60
nameji = total % 60
print(mok)
print(nameji)
