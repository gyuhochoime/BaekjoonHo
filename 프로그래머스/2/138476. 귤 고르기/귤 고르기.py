def solution(k, tangerine):
    dic = dict()
    arr = []
    tmp = k
    cnt = 0
    for i in tangerine:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    for key, value in dic.items():
        arr.append((key, value))
    arr.sort(key = lambda x: (-x[1]))
    for key, value in arr:
        if tmp <= 0:
            break
        tmp -= value
        cnt += 1
    return cnt