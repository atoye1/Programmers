const fs = require('fs');

const input = fs.readFileSync('/dev/stdin').toString().split('\n');
const count = input[0];
const stack = [];
const result = [];

for (let i = 1; i <= count; i++) {
  const command = input[i].split(' ')[0];
  // console.log(command);
  switch (command) {
    case 'push':
      stack.push(parseInt(input[i].split(' ')[1], 10));
      break;
    case 'pop':
      if (stack.length === 0) {
        result.push(-1);
      } else {
        result.push(stack.pop());
      }
      break;
    case 'size':
      result.push(stack.length);
      break;
    case 'empty':
      if (stack.length === 0) {
        result.push(1);
      } else {
        result.push(0);
      }
      break;
    case 'top':
      if (stack.length === 0) {
        result.push(-1);
      } else {
        result.push(stack[stack.length - 1]);
      }
      break;
    default:
      break;
  }
}

console.log(result.join('\n'));
