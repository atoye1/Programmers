def solution(clothes):
    answer = 1
    hash_map = {}
    for cloth, category in clothes:
        hash_map.setdefault(category, 0)
        hash_map[category] += 1
    for key, value in hash_map.items():
        # 아무것도 선택하지 않는 경우를 가정해야하므로 1을 더한 값을 곱한다.
    	answer *= (value + 1)
        
    # 아무것도 입지 않는 경우는 없으므로 제외한다.
    return answer - 1