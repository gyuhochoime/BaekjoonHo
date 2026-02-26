arr = [0] * 11111
a = 1
for i in range(1, 10001):
    x = i
    for j in str(x):
        x += int(j)
    arr[x] = 1
for i in range(1, 10001):
    if arr[i] == 0:
        print(i)
