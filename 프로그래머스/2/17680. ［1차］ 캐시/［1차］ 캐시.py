from collections import deque

def solution(cacheSize, cities):
    answer = 0
    arr = deque()
    if cacheSize == 0:
        return 5 * len(cities)
    for i in cities:
        i = i.upper()
        if i in arr:
            arr.remove(i)
            arr.append(i)
            answer += 1
        else:
            if len(arr) == cacheSize:
                arr.popleft()
            arr.append(i)
            answer += 5
    return answer