function solution(hp) {
    let answer = 0
    if (hp / 5 >= 1) {
        answer += Math.floor(hp / 5)
        hp %= 5
    }
    if (hp / 3 >= 1) {
        answer += Math.floor(hp / 3)
        hp %= 3
    }
    answer += hp
    return answer
}