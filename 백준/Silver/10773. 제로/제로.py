import sys

count = int(sys.stdin.readline())
total = 0
stack = []
while count:
    current = int(sys.stdin.readline())
    if current == 0:
        total -= stack.pop()
    else:
        stack.append(current)
        total += current
    count -= 1
print(total)
