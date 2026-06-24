from collections import deque
def solution(numbers, direction):
    numbers = deque(numbers)
    if direction == "right":
        numbers.appendleft(numbers.pop())
    elif direction == "left":
        numbers.append(numbers.popleft())
    answer = numbers
    return list(answer)