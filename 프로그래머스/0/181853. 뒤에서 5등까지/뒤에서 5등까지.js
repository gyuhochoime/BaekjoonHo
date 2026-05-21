function solution(num_list) {
    let answer = [...num_list]
    answer.sort((a, b) => a - b)
    let arr = answer.slice(0, 5)
    return arr
}