def solution(people, limit):
    cnt = 0
    people.sort()
    lt = 0
    rt = len(people) - 1
    while lt <= rt:
        if people[lt] + people[rt] > limit:
            rt -= 1
            cnt += 1
        elif people[lt] + people[rt] <= limit:
            lt += 1
            rt -= 1
            cnt += 1
    return cnt