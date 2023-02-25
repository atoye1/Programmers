function solution(participant, completion) {
    const counter = {};
    const maxLen = participant.length;
    for (let i = 0; i < maxLen; i++) {
       if (!counter[participant[i]]) counter[participant[i]] = 0;
       if (!counter[completion[i]]) counter[completion[i]] = 0;
       counter[participant[i]]++;
       counter[completion[i]]--;
    }
    
    for (let k in counter) {
        if (counter[k] > 0) return k;
    }
    return null;
}