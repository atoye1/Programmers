def solution(clothes):
    answer = 1
    hash_map = {}
    for cloth, category in clothes:
        if not hash_map.get(category):
            hash_map[category] = 1
        else:
            hash_map[category] += 1
    for key, value in hash_map.items():
    	answer *= (value + 1)
        
    # 아무것도 입지 않는 경우는 없으므로 제외한다.
    return answer - 1