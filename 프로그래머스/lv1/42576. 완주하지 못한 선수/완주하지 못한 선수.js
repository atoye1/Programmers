function solution(participant, completion) {
    let answer = '';
    participant = participant.sort();
    completion = completion.sort();
    for (i = 0; i < completion.length - 1; i++) {
        if (participant[i] !== completion[i]) {
            return participant[i];
        }
    }
    return participant[participant.length - 1];
}