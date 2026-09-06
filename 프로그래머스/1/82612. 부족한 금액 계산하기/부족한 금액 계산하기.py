def solution(price, money, count):
    tot = 0
    for i in range(1, count + 1):
        tot += price * i
    if tot >= money:
        return tot - money
    else:
        return 0