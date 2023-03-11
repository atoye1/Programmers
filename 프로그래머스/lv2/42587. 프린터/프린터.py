from collections import deque

def solution(priorities, location):
    answer = 0
    q = deque(enumerate(priorities))
    while q:
        max_rank = max([i[1] for i in q])
        idx, rank = q.popleft()
        if rank < max_rank:
            q.append((idx, rank))
        else:
            answer += 1
            if idx == location:
                return answer