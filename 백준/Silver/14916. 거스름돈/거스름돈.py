import sys
n = int(sys.stdin.readline().rstrip())
su = n % 10
m = 0
cnt = 0
if n == 1 or n == 3:
    cnt = -1
elif su == 0 or su == 5:
    cnt += n // 5
elif su == 1 or su == 6:
    m = n - 2 * 3
    cnt += 3
    cnt += m // 5
elif su == 2 or su == 7:
    m = n - 2 * 1
    cnt += 1
    cnt += m // 5
elif su == 3 or su == 8:
    m = n - 2 * 4
    cnt += 4
    cnt += m // 5
elif su == 4 or su == 9:
    m = n - 2 * 2
    cnt += 2
    cnt += m // 5
print(cnt)
