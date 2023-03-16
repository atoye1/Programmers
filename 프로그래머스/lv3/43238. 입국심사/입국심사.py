'''
	10억 이니깐 선형시간으로도 안됨.
    그래서 큐를 활용해서 순차적으로 풀이하면 시간초과가 나올것이다.
    로그시간으로 풀어야된다.
    문제의 분류에도 있듯이 이분탐색으로 풀이해야함.
    보통 이분탐색은 결과를 대상으로 수행함.
    따라서 결과의 최솟값과 최대값을 구하고, 그것들을 이분탐색적으로 대입해서 푼다.
    파라메트릭서치라고 했는데, 최적화 문제를 결정문제로 변환해서 푸는 것이다.
'''

'''
1. 만약 모든 사람이 한개의 심사대에서만 심사를 받는다면 걸리는 시간은 n * time 이다.
2. 심사하는데 걸리는 최대한의 시간은 customer / worker * max(times)다.
3. 심사하는데 걸리는 최소한의 시간은 customer / worker * min(times)다.
4. times배열은 10만 이하니까 정렬해도 괜찮다.
5. 잠깐, 이분탐색은 정렬한 것을 대상으로 하는거니깐 times를 대상으로 이분탐색 하는거야?
	아닌것같은데...
'''


def solution(n, times):
    answer = 0
    times.sort()
    max_time = int(n * min(times))
    # 만약 최솟값인 심사대에서 모든 처리를 다하는 상황을 가정하면, 최대 소모시간은 아래와 같다.
    # 최소 소모시간은 1로 잡는다
    # 1과 max_time 사이를 이분탐색해본다.
    start = 1
    end = max_time
    people = 0
    print(max_time)
    while start <= end:
        # mid초 안에 입국심사가 완료 가능한지 판별해야 한다.
        mid = (start + end) // 2
        # mid초가 걸렸을 때 처리할 수 있는 사람들의 총 합은
        people = sum([mid // time for time in times])
        print('mid', mid, 'people', people)
        if people >= n: # 조건을 만족한 경우이므로 더 작은쪽을 탐색한다.
            answer = mid
            end = mid - 1
        else: # 조건을 불만족했으므로 더 큰쪽을 탐색해야 한다.
            start = mid + 1
    return answer

