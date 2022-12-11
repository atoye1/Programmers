function solution(progresses, speeds) {
    var answer = [];
    let pointer = 0;
    
    while (pointer < progresses.length) {
        let multiplier = Math.ceil((100 - progresses[pointer]) / speeds[pointer]);
        // update progresses until first job is done
		for (let i = pointer; i < progresses.length; i++) {
            progresses[i] += (multiplier * speeds[i]);
        }
        console.log(multiplier)
        console.log(progresses)
        // count done job
        let count = 0;
        for (let i = pointer; i < progresses.length; i++) {
            if (progresses[i] >= 100) {
                pointer++;
                count++;
            } else {
                break;
            }
        }
        answer.push(count)
    }
    return answer;
}