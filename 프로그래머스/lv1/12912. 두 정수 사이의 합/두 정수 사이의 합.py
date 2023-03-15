from itertools import accumulate

'''
1. 간단히 파이썬 라이브러리를 활용하면 구할 수 있다.
2. 하드 코딩보다 성능이 우수하다.
'''

def solution(a, b):
    # a가 크면 둘을 스왑해주자.
    if a > b:
        a, b = b, a
        
    answer = sum(range(a, b + 1))
    
    return answer