from itertools import permutations
import math

# numbers의 길이가 7에 불과해서 다항시간처럼 비효율적인 알고리즘을 사용해도 된다.
# 조합이나 순열 등의 완전탐색도 가능하다는 의미다.

def is_prime(num):
    if num == 1 or num == 0:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def solution(numbers):
    l = list(numbers)
    checked_num = set()
    for i in range(1, len(numbers) + 1):
        p = permutations(l, i)
        for elem in p:
            num = int(''.join(elem))
            if is_prime(num) and num not in checked_num:
                checked_num.add(num)
    return len(checked_num)