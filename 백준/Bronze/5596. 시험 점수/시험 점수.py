s = list(map(int, input().split()))
t = list(map(int, input().split()))
n = 0
m = 0
for i in range(len(s)):
    n += s[i]
for j in range(len(t)):
    m += t[j]
if n >= m:
    print(n)
else:
    print(m)
