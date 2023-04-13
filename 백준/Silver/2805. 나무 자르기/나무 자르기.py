# 이거 떡볶이 떡 자르기처럼 파라메트릭 서치 문제 아냐?
# 파라미터를 뭘로 설정하느냐가 중요하고, 이분탐색을 하는게 중요하다.
# 파라미터의 범위는 0부터 백만이다.
# 나무의 개수는 백만개니깐 O(N)연산을 적용해도 된다.
# 길이는 10억이니까 O(logN)을 사용해야 한다.

import sys
N, M = map(int, sys.stdin.readline().rstrip().split())
trees = list(map(int, sys.stdin.readline().split()))

start = 0
end = 1_000_000_000

result = 0
while (start <= end):
    mid = (start + end) // 2
    total = 0
    for tree in trees:
        if tree > mid:
            total += tree - mid
    if total > M:  # 현재 자른 나무의 합이 목표보다 크다. 따라서 자르는 길이를 올려서 더 적게 자를 수 있는지 파악해야 한다.
        result = mid
        start = mid + 1
    elif total == M:
        result = mid
        break
    else:  # 길이 조건 불만족시 자르는 높이를 내려야한다.
        end = mid - 1

print(result)
