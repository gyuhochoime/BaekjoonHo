import sys
n = list(map(str, sys.stdin.readline().strip().split("-")))
arr = []
for i in n:
    tot = 0
    tmp = i.split("+")
    for j in tmp:
        tot += int(j)
    arr.append(tot)
final_tot = 0
for i in arr:
    final_tot -= i
final_tot += arr[0] * 2
print(final_tot)
