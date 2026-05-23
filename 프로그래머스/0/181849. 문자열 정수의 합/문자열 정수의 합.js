function solution(num_str) {
    let answer = 0
    const num = num_str.split('').map(Number)
    for (let i = 0; i < num.length; i++)
        {
            answer += num[i]
        }
    return answer
}