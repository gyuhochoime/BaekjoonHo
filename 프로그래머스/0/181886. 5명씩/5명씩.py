def solution(names):
    people = len(names)
    arr = []
    for i in range(0, people, 5):
        arr.append(names[i])
    return arr