import sys
n = list(sys.stdin.readline().rstrip())
rh = 0
lh = 0
standard = 0
for i in range(len(n)):
    if n[i] == "0":
        standard = i
for i in range(len(n)):
    if n[i] == "@" and i < standard:
        rh += 1
    elif n[i] == "@" and i > standard:
        lh += 1
print(rh, lh)
        
