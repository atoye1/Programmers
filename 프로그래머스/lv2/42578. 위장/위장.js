function solution(clothes) {
    var answer = 0;
    const counter = {};
    clothes.forEach(elem => {
        counter[elem[1]] = (counter[elem[1]] || 1) + 1;
    })
    return Object.values(counter).reduce((acc, cur) => acc * cur) - 1;
    return answer;
}