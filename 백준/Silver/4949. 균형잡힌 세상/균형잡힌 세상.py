from collections import deque
while True:
    text = input()
    if text == '.':
        break

    _text = deque([c for c in text if c in ['[', ']', '(', ')', '{', '}']])
    if len(_text) == 0:
        print('yes')
        continue

    stack = deque()
    isCorrect = True
    while _text:
        curr = _text.popleft()
        if curr in ['[', '(', '{']:
            stack.append(curr)
        else:
            if len(stack) == 0:
                isCorrect = False
                break
            before = stack.pop()
            gap = ord(curr) - ord(before)
            if gap != 1 and gap != 2:
                isCorrect = False
                break

    if len(stack) != 0:
        isCorrect = False

    if isCorrect:
        print('yes')
    else:
        print('no')
