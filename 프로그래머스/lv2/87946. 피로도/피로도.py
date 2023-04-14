from itertools import permutations

def solution(k, dungeons):
    answer = -1
    # 던전이 총 8개 밖에 안되니깐 8! 40320번 비교하면 되니깐 완전탐색가능
    # 10! 정도는 완전탐색 할 수 있다고 보면된다.
    
    # 완전탐색이면 순열로 섞어서 무식하게 풀어보고, 최적값을 리턴하면 된다.
    candidates = permutations(dungeons)
    for case in candidates:
        energy = k
        visited = 0
        for d in case:
            if energy >= d[0]:
                energy -= d[1]
                visited += 1
            else:
                break
        answer = max(answer, visited) 
    
    return answer