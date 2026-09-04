def solution(record):
    dic = dict()
    logs = []
    answer = []
    for i in record:
        arr = i.split()
        if arr[0] == "Enter":
            dic[arr[1]] = arr[2]
            logs.append(("Enter", arr[1]))
        elif arr[0] == "Leave":
            logs.append(("Leave", arr[1]))
        elif arr[0] == "Change":
            dic[arr[1]] = arr[2]
    for key, value in logs:
        if key == "Enter":
            answer.append(dic[value] + "님이 들어왔습니다.")
        elif key == "Leave":
            answer.append(dic[value] + "님이 나갔습니다.")
    return answer