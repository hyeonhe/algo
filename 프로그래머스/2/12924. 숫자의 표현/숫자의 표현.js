function solution(n) {
    let answer = 0
    for (let i=1; i<=n; i++){
        let sum = i
        
        for (let j=i+1; sum<=n; j++) {
            
            if (n === sum) {
                answer += 1
            } 
            sum += j

        }
    }
    
    return answer;
}