from collections import deque

def solution(people, limit):
    answer = 0
    people.sort()
    people = deque(people)
    
    p1 = 0
    p2 = len(people) - 1
    
    while people:
        largest = people.pop()
        if not people:
            pass
        elif largest + people[0] > limit:
            pass
        else:
            smallest = people.popleft()
        answer += 1
    return answer