function solution(s) {
    const answer = []
    const lastOccurrence = {};
    
    for (let i = 0; i < s.length; i++){
        const char = s[i]
        if (char in lastOccurrence){
            answer.push(i - lastOccurrence[char])
        } else {
            answer.push(-1)
        }
        lastOccurrence[char] = i
    }
    return answer;
}