import sys
n, m = map(str, sys.stdin.readline().rstrip().split())
people = set()
for _ in range(int(n)):
    a = sys.stdin.readline().rstrip()
    people.add(a)
num = len(people)
cnt = 0
if m == "O":
    su = 3
elif m == "F":
    su = 2
elif m == "Y":
    su = 1
while num >= su:
    num -= su
    cnt += 1
print(cnt)
