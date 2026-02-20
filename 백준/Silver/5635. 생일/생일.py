import sys
n = int(sys.stdin.readline())
student = []
for _ in range(n):
    name, day, mon, year = map(str, sys.stdin.readline().split())
    student.append((name, int(day), int(mon), int(year)))
student.sort(key = lambda x: (x[3], x[2], x[1]))
print(student[-1][0])
print(student[0][0])
