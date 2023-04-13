count = int(input())
total = 0
stack = []
while count:
    current = int(input())
    if current == 0:
        stack.pop()
    else:
        stack.append(current)
    count -= 1
print(sum(stack))
