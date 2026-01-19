import sys
words = []
for _ in range(5):
    a = sys.stdin.readline().rstrip()
    words.append(a)
sero = ""
m = 0
for i in words:
    m = max(len(i), m)
for i in range(m):
    for j in range(5):
        if i < len(words[j]):
            sero += words[j][i]
print(sero)
