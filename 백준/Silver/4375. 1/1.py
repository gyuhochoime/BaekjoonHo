import sys
while True:
    try:
        n = int(sys.stdin.readline())
        a = "1"
        cnt = 1
        while True:
            if int(a) % n == 0:
                break
            else:
                a += "1"
                cnt += 1
        print(cnt)
    except:
        break
