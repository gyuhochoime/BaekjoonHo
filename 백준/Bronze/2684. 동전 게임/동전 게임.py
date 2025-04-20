import sys
T = int(sys.stdin.readline().rstrip())
for i in range(T):
    n = sys.stdin.readline().rstrip()
    arr = [0] * 8
    for j in range(38):
        if n[j:j+3] == "TTT":
            arr[0] += 1
        elif n[j:j+3] == "TTH":
            arr[1] += 1
        elif n[j:j+3] == "THT":
            arr[2] += 1
        elif n[j:j+3] == "THH":
            arr[3] += 1
        elif n[j:j+3] == "HTT":
            arr[4] += 1
        elif n[j:j+3] == "HTH":
            arr[5] += 1
        elif n[j:j+3] == "HHT":
            arr[6] += 1
        elif n[j:j+3] == "HHH":
            arr[7] += 1
    print(*arr)
