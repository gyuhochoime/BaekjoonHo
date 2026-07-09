def solution(N, stages):
    arr = []
    dic = {i: 0 for i in range(1, N + 1)}
    lst = []
    answer = []
    tot = len(stages)
    for i in stages:
        if i in dic:
            dic[i] += 1
        elif i not in dic and i != N + 1:
            dic[i] = 1
    for key, value in dic.items():
        arr.append((key, value))
    arr.sort(key = lambda x: x[0])
    for key, value in arr:
        if tot == 0:
            lst.append((key, 0))
        else:
            lst.append((key, value / tot))
            tot -= value
    lst.sort(key = lambda x: -x[1])
    for key, value in lst:
        answer.append(key)
    return answer