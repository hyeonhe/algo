function solution(name, yearning, photo) {
    const answer = [];
    const nameMap = {};
    
    name.forEach((item, i) => {
        nameMap[item] = yearning[i]
    })
    
    photo.forEach((arr) => {
        let score = 0;
        arr.forEach((item) => {
            if (item in nameMap) {
                score += nameMap[item]
                console.log(score)
            }
        })
        console.log(score)
        answer.push(score)
    })
    return answer;
}