function solution(participant, completion) {
    var answer = '';
    const counter = {};
    participant.forEach(person => {
        counter[person] = (counter[person] || 0) + 1;
    })
    completion.forEach(person => {
        counter[person]--;
        if (counter[person] === 0) delete counter[person];
    })
    return Object.keys(counter)[0];
}