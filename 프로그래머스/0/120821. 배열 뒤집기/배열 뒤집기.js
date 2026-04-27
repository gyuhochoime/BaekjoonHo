function solution(num_list) {
    let answer = []
    const tmp = num_list.length
    for (let i = 0; i < tmp; i++) {
        answer.push(num_list.pop())
    }
    return answer
}