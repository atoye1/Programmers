function solution(progresses, speeds) {
    var answer = [];
    let pointer = 0;
    
    while (pointer < progresses.length) {
        let multiplier = Math.ceil((100 - progresses[pointer]) / speeds[pointer]);
        // update progresses until first job is done
		for (let i = pointer; i < progresses.length; i++) {
            progresses[i] += (multiplier * speeds[i]);
        }
        // count done jobs and append to answer
        let count = 0;
        for (let i = pointer; i < progresses.length; i++) {
            if (progresses[i] >= 100) {
                pointer++;
                count++;
            } else { // if job is not 100%, need to finish this job with multiplier
                break;
            }
        }
        answer.push(count)
    }
    return answer;
}