function solution(n, lost, reserve) {
    const net_lost = lost.filter(elem => !reserve.includes(elem)).sort();
    const net_reserve = reserve.filter(elem => !lost.includes(elem)).sort();
    const initLost = net_lost.length;
    let lended = 0;
    
    while (net_lost.length !== 0) {
        const current = net_lost.pop();
        for (let i = net_reserve.length - 1; i >= 0; i--) {
            if (current + 1 === net_reserve[i] || current - 1 === net_reserve[i]) {
                lended++;
                net_reserve.splice(i,1)
                break;
            }
        }
    }

    var answer = n - initLost + lended;
    return answer;
}