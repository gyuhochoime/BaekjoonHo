function solution(num_list, n) {
    let answer = 0
    for (a of num_list) {
        if (a === n) {
            answer = 1
            break
        }
    }
    return answer
}