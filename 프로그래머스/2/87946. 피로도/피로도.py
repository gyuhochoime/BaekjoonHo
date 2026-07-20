def solution(k, dungeons):
    answer = 0
    stack = [(k, 0, [False] * len(dungeons))]
    while stack:
        fatigue, cnt, visited = stack.pop()
        answer = max(answer, cnt)
        for i in range(len(dungeons)):
            key, value = dungeons[i]
            if not visited[i] and fatigue >= key:
                new_visited = visited[:]
                new_visited[i] = True
                stack.append((fatigue - value, cnt + 1, new_visited))
    return answer