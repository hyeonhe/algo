function solution(a, b, n) {
    let answer = 0;
    let coke = n;
    
    while (coke >= a){
        let quotient = Math.floor(coke / a)
        answer += quotient * b
        coke -= quotient * a
        coke += quotient * b
    }
    return answer;
}