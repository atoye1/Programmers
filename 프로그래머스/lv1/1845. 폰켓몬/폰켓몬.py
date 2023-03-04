def solution(nums):
    monster_set = set(nums)
    print(len(monster_set), len(nums))
    answer = len(monster_set) if len(monster_set) < len(nums) // 2 else len(nums) // 2
    return answer