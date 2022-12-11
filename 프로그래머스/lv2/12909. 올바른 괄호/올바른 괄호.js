function solution(s){
    if (s[0] === ')') return false;
    const stack = [];
    for (let i = 0; i < s.length; i++) {
        if (s[i] === '(') {
            stack.push(s[i]);
        } else if (s[i] === ')') {
            if (!stack.pop() === '(')  return false;
        }
    }
    if (stack.length === 0)  return true;
    return false;
}