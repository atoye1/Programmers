import math
from collections import deque

def solution(progresses, speeds):
    answer = []
    p_q = deque(progresses)
    s_q = deque(speeds)
    counts = deque()
    
    while p_q:
        count = math.ceil((100 - p_q.popleft()) / s_q.popleft())
        counts.append(count)
        
    while counts:
        curr_count = counts.popleft()
        completed = 1
        while True and counts:
            if counts[0] <= curr_count:
                counts.popleft()
                completed += 1
            else:
                break
        answer.append(completed)
    return answer



def solution(progresses, speeds):
    print(progresses)
    print(speeds)
    answer = []
    time = 0
    count = 0
    while len(progresses)> 0:
        if (progresses[0] + time*speeds[0]) >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        else:
            if count > 0:
                answer.append(count)
                count = 0
            time += 1
    answer.append(count)
    return answer