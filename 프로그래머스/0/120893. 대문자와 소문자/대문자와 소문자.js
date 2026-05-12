function solution(my_string) {
    let answer = ''
    for (const ch of my_string) {
        if (ch === ch.toUpperCase()) {
            answer += ch.toLowerCase()
        } else {
            answer += ch.toUpperCase()
        }
    }
    return answer
}