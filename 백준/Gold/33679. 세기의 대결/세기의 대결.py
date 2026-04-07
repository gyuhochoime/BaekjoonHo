import sys
n = int(sys.stdin.readline())
arr_1 = list(map(int, sys.stdin.readline().split()))
arr_2 = list(map(int, sys.stdin.readline().split()))
max_dp_1 = max_dp_2 = 0
for s in range(n):
    dp_1 = [1] * n
    dp_2 = [1] * n
    for i in range(1, n):
        for j in range(i):
            if arr_1[(s + i) % n] > arr_1[(s + j) % n]:
                dp_1[i] = max(dp_1[i], dp_1[j] + 1)
            if arr_2[(s + i) % n] > arr_2[(s + j) % n]:
                dp_2[i] = max(dp_2[i], dp_2[j] + 1)
    max_dp_1 = max(max_dp_1, max(dp_1))
    max_dp_2 = max(max_dp_2, max(dp_2))
if max_dp_1 > max_dp_2:
    print("YJ Win!")
elif max_dp_1 == max_dp_2:
    print("Both Win!")
elif max_dp_1 < max_dp_2:
    print("HG Win!")