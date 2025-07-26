import sys
T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    arr = []
    tot = 0
    while True:
        n = int(sys.stdin.readline().rstrip())
        if n == 0:
            break
        arr.append(n)
    arr.sort(reverse = True)
    for i in range(len(arr)):
        tot += 2 * (arr[i] ** (i + 1))
    if tot <= 5000000:
        print(tot)
    else:
        print("Too expensive")
