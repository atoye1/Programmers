def solution(numbers):
    s_nums = list(map(str, numbers))
    
    s_nums.sort(reverse=True)
    s_nums.sort(key= lambda x : x*3, reverse=True) 
    
    answer = str(int(''.join(s_nums)))
    return answer