import sys
input = sys.stdin.readline  # 입력시간을 줄이기 위해 stdin 사용한다.

house_count, router_count = map(int, input().split())
houses = []
for i in range(house_count):
    houses.append(int(input()))
houses.sort()  # 파라메트릭 서치로 이분탐색해야하므로 정렬하는게 편하다.

'''
파라메트릭서치 문제다.
파라미터가 뭔지 정해야 한다.
여기선 간격을 파라미터로 정한다.
1. 그렇다면 파라미터의 가능한 구간을 정해야 한다.
최소간격은 1이 될 것이고
최대 간격은 집 좌표의 최대값이 될것이다.

2. 이분탐색의 대상인 간격으로 공유기를 배치할 수 있는지
따져보는 로직이 필요하다.

3. 만약 해당 간격으로 공유기 설치가 가능하다면 더 큰 구간을 탐색하고
설치가 불가능하면 작은 구간을 탐색한다.

4. 탐색이 끝나면 최적해를 반환해야한다.
'''


def is_possible(houses, interval, count):
    # 마지막에 공유기가 배치된 인덱스를 저장하는 변수 선언.
    last_idx = 0
    count -= 1  # 최초의 집엔 무조건 배치하므로 count를 1 빼준다.
    for i in range(1, len(houses)):
        # 현재 계산하는 집과 마지막에 공유기가 배치된 집의 간격이 인터벌보다 크거나 같으면
        if houses[i] - houses[last_idx] >= interval:
            # 배치해야할 공유기 갯수를 1 줄이고
            count -= 1
            # 마지막에 배치한 인덱스를 갱신해준다.
            last_idx = i
        # count가 0이란건 모든 공유기를 배치한것이므로 True 반환한다.
        if count == 0:
            return True
    return False


# 최소 인터벌은 항상 1이다.
start = 1
# 최대 인터벌은 최댓값 - 최솟값이다.
end = houses[-1] - houses[0]
# answer의 초깃값은 항상 최소.
answer = 1
while start <= end:
    mid = (start + end) // 2
    # 만약 현재 인터벌로 배치하는게 가능하다면, 오른쪽 절반을 살펴본다.
    if is_possible(houses, mid, router_count):
        start = mid + 1
        answer = max(answer, mid)
    else:  # 현재 인터벌로 배치하는게 불가능하면 왼쪽, 더 작은 범위를 살펴봐야한다.
        end = mid - 1

print(answer)
