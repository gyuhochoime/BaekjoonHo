import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
arr.sort()
if abs(arr[0]) > abs(arr[n-1]):
    tot = abs(arr[0])
    arn = []
    arm = []
    for i in arr:
        if i >= 0:
            arn.append(i)
        else:
            arm.append(abs(i))
    arn.sort()
    arm.sort()
    for i in range(m):
        if len(arm) > 0:
            arm.pop()
    while len(arn) > 0:
        tot += arn[len(arn)-1] * 2
        for i in range(m):
            if len(arn) > 0:
                arn.pop()
    while len(arm) > 0:
        tot += arm[len(arm)-1] * 2
        for i in range(m):
            if len(arm) > 0:
                arm.pop()
    print(tot)
else:
    tot = abs(arr[n-1])
    arn = []
    arm = []
    for i in arr:
        if i >= 0:
            arn.append(i)
        else:
            arm.append(abs(i))
    arn.sort()
    arm.sort()
    for i in range(m):
        if len(arn) > 0:
            arn.pop()
    while len(arn) > 0:
        tot += arn[len(arn)-1] * 2
        for i in range(m):
            if len(arn) > 0:
                arn.pop()
    while len(arm) > 0:
        tot += arm[len(arm)-1] * 2
        for i in range(m):
            if len(arm) > 0:
                arm.pop()
    print(tot)
    
