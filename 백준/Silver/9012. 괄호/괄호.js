const fs = require('fs');

const input = fs.readFileSync('/dev/stdin').toString().split('\n');
const count = input[0];
const result = [];
for (let i = 1; i <= count; i++) {
  const str = input[i];
  const stack = [];
  let isValid = true;
  for (const char of str) {
    if (char === '(') {
      stack.push(char);
    } else if (stack.pop() !== '(') {
      isValid = false;
      break;
    }
  }
  if (stack.length === 0 && isValid) {
    result.push('YES');
  } else {
    result.push('NO');
  }
}

console.log(result.join('\n'));
