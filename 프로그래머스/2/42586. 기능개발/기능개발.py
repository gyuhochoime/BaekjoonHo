from collections import deque
def solution(progresses, speeds):
    arr = []
    progresses = deque(progresses)
    speeds = deque(speeds)
    while progresses:
        cnt = 0
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        while progresses:
            if progresses[0] >= 100:
                progresses.popleft()
                speeds.popleft()
                cnt += 1
            else:
                break
        if cnt > 0:
            arr.append(cnt)
    return arr