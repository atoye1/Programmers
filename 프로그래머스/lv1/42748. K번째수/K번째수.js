function solution(array, commands) {
    var answer = [];
    commands.forEach(elem => {
        [start, end, index] = elem;
        console.log(start, end, index)
        let val = array.slice(start - 1, end).sort((a, b) => a - b)[index - 1];
        answer.push(val);
    })
    return answer;
}