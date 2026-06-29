from collections import deque
def solution(board, moves):
    answer = 0
    arr = deque(board)
    a = len(board)
    for i in range(a):
        arr[i] = deque(arr[i])
    stack = []
    for i in moves:
        for j in range(a):
            if arr[j][i-1] != 0:
                for k in range(i-1):
                    arr[j].append(arr[j].popleft())
                tmp = arr[j].popleft()
                arr[j].append(0)
                if len(stack) == 0:
                    stack.append(tmp)
                else:
                    if stack[-1] == tmp:
                        stack.pop()
                        answer += 2
                    else:
                        stack.append(tmp)
                for k in range(i):
                    arr[j].appendleft(arr[j].pop())
                break
    return answer