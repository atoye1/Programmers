function solution(numbers) {
    const callback = (a, b) => {
        a = a.toString();
        b = b.toString();
        return parseInt(b + a) - parseInt(a + b)
    }
    numbers.sort(callback)
    if (numbers[0] === 0) return '0';
    return numbers.join('');
}