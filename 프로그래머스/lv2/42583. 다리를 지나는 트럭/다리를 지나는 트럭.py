from collections import deque
def solution(bridge_length, weight, truck_weights):
    # 시간대별로 스냅샷을 큐에 저장하면서 풀이한다.
    # 큐에 새로운 요소가 들어와도 되는지 판별하는 것이 포인트다.
    # 큐에 빈자리가 하나 있고, 현재 무게를 추가했을 때 큐에 들어 있는 전체 무게가 오버되지 않으면
    # 새로운 트럭을 들어오게 할 수 있다.
    # 새로운 트럭 진입이 불가능하면 시간을 늘려서 기다린다.
    time = 0
    truck_q = deque(truck_weights)
    bridge_q = deque([0 for _ in range(bridge_length)])
    current_sum = 0
    
    while True:
        current_sum -= bridge_q.popleft()
        time += 1
        # 당연히 마지막 요소가 빈다.
        # 다리에 있는 모든 앞선 트럭의 합과 현재 들어오려는 트력의 합이 제한보다 작으면 삽입.
        # sum()을 호출하면 시간초과가 나오니 다이나믹 프로그래밍 방식으로 sum을 기록해나간다.
        if truck_q:
            if current_sum + truck_q[0] <= weight:
                current_sum += truck_q[0]
                bridge_q.append(truck_q.popleft())
            else:
                bridge_q.append(0)
        # 만약 대기트럭이 하나도 없으면 브릿지에 있는 트럭을 앞으로 한번씩 민다.
        else:
            return time + bridge_length - 1