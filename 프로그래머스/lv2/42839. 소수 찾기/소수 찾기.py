from itertools import permutations
import math

def is_prime(num):
    if num == 1 or num == 0:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    l = list(numbers)
    checked_num = set()
    for i in range(1, len(numbers) + 1):
        p = permutations(l, i)
        for elem in p:
            num = int(''.join(elem))
            print(num)
            if is_prime(num):
                if num not in checked_num:
                    checked_num.add(num)
                    answer += 1
    print(checked_num)
    return answer