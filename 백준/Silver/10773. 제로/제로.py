count = int(input())
total = 0
stack = []
while count:
    current = int(input())
    if current == 0:
        total -= stack.pop()
    else:
        stack.append(current)
        total += current
    count -= 1
print(total)
