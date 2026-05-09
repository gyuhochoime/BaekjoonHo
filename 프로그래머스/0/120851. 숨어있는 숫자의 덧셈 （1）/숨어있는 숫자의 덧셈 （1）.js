function solution(my_string) {
    let answer = 0
    for (const a of my_string) {
        if (/\d/.test(a)) {
            answer += Number(a)
        }
    }
    return answer
}