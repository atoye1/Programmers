from collections import Counter

def solution(participant, completion):
    pc = Counter(participant)
    cc = Counter(completion)
    rc = pc - cc
    return list(rc.keys())[0]
