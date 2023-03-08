from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0
    answer = bfs(begin, target, words)
    return answer

def bfs(begin, target, words):
    q = deque()
    visited = []
    q.append((begin, 0))
    while q:
        curr = q.popleft()
        if curr[0] == target:
            return curr[1]
        else:
            for word in words:
                if is_valid(curr[0], word) and word not in visited:
                    q.append((word, curr[1] + 1))
    return 0

def is_valid(origin, target):
    threshold = 0
    for i in range(len(origin)):
        if origin[i] != target[i]:
            threshold += 1
            if threshold > 1:
                return False
    return True if threshold == 1 else False
    