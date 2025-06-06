import sys
n = sys.stdin.readline().rstrip()
n = list(n.upper())

dic1 = {}
for i in n:
    if i in dic1:
        dic1[i] += 1
    else:
        dic1[i] = 1

max_count = max(dic1.values())
max_chars = [char for char, count in dic1.items() if count == max_count]

if len(max_chars) > 1:
    print('?')
else:
    print(max_chars[0])
