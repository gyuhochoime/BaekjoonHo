import sys
while True:
    cnt = 0
    n = list(sys.stdin.readline().rstrip())
    if n == ["#"]:
        break
    for i in n:
        if i == "1":
            cnt += 1
    if n[len(n)-1] == "e" and cnt % 2 == 0:
        n[len(n)-1] = 0
    elif n[len(n)-1] == "e" and cnt % 2 == 1:
        n[len(n)-1] = 1
    elif n[len(n)-1] == "o" and cnt % 2 == 0:
        n[len(n)-1] = 1
    elif n[len(n)-1] == "o" and cnt % 2 == 1:
        n[len(n)-1] = 0
    for i in n:
        print(i, end = "")
    print()
