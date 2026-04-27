function solution(money) {
    let answer = []
    const cup = Math.floor(money / 5500)
    const change = money - cup * 5500
    answer.push(cup)
    answer.push(change)
    return answer
}