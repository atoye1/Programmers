from collections import deque

def solution(bridge_length, weight, truck_weights):
    # 시간대별로 스냅샷을 큐에 저장하면서 풀이한다.
    # 큐에 새로운 요소가 들어와도 되는지 판별하는 것이 포인트다.
    # 큐에 빈자리가 하나 있고, 현재 무게를 추가했을 때 큐에 들어 있는 전체 무게가 오버되지 않으면
    # 새로운 트럭을 들어오게 할 수 있다.
    # 새로운 트럭 진입이 불가능하면 시간을 늘려서 기다린다.
    answer = 0
    truck_q = deque(truck_weights)
    bridge_q = deque([0 for _ in range(bridge_length)])
    bridge_sum = 0
    
    while True:
        answer += 1
        bridge_sum -= bridge_q.popleft()
        # 당연히 마지막 요소가 빈다.
        # 다리에 있는 모든 앞선 트럭의 합과 현재 들어오려는 트력의 합이 제한보다 작으면 삽입.
        # sum()을 호출하면 시간초과가 나오니 다이나믹 프로그래밍 방식으로 sum을 기록해나간다.
        # 리스트의 sum()은 O(n) 시간인데, 이걸 O(1)으로 개선하니 시간에 맞게 풀이할 수 있었다.
        if truck_q:
            if bridge_sum + truck_q[0] <= weight:
                bridge_sum += truck_q[0]
                bridge_q.append(truck_q.popleft())
            else:
                bridge_q.append(0)
        else:
            # 대기하는 트럭이 없는 경우엔 한번에 계산해서 경과시간을 구할 수 있다.
            return answer + bridge_length - 1

# 신기하다.
# 코테실력이 점점 느는게 느껴진다.
# 예전에는 풀이를 도저히 생가할 수 없었던 문제들도 풀이가 생각나고
# 차분히 구현하니 정답이 나온다.
# 못할 공부는 없다. 열심히하고 똑바로 하면 다 할 수 있다.
# 알고리즘 열심히 공부해서 해외 유명 IT 기업에 취직할거다. 꼭