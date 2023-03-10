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
            answer += 1
        elif largest + people[0] > limit:
            answer += 1
        else:
            smallest = people.popleft()
            sum = largest + smallest
            while people and sum + people[0] <= limit:
                sum += people.popleft()
            answer += 1
    return answer