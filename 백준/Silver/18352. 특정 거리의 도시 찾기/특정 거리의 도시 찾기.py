import sys
from collections import deque

input = sys.stdin.readline

city_count, road_count, target_distance, start_city = map(int, input().split())

# roads.sort(key=lambda x: x[0])  # 앞의 숫자를 기준으로 정렬한다.

# 1번부터 다뤄야 하므로 range에서 + 1을 해야한다.
graph = [[] for _ in range(city_count + 1)]  
for _ in range(road_count):
    a, b = map(int, input().split())
    graph[a].append(b)

# graph를 대상으로 bfs하고, 그 결과를 distances 배열에 저장하면 될라나?
# distance를 기록할 배열을 초기화해준다.
# 초깃값을 -1로 안해줘서 틀렸나?
distances = [-1 for _ in range(city_count + 1)]
distances[start_city] = 0


def bfs(graph, start, distances):
    q = deque()
    q.append(start)
    while q:
        curr = q.popleft()
        current_dist = distances[curr]  # 현재 도시의 거리를 구한다.
        candidates = graph[curr]  # 그래프에서 현재와 연결된 도시들을 전부다 불러온다.
        # 만약 거리가 0으로 처음 방문하는 도시인 경우는
        candidates = [i for i in candidates if distances[i] == -1]
        # 현재 도시의 거리 + 1로 거리를 갱신해준다.
        for i in candidates:
            distances[i] = current_dist + 1
        q.extend(candidates)


# 너비우선 탐색을해서 distances 배열을 완성한다.
bfs(graph, start_city, distances)
# 만약 조건을 만족하는 도시가 없는 경우 처리를 위해 선언해준다.
is_printed = False

for idx, num in enumerate(distances):
    if num == target_distance:
        is_printed = True
        print(idx)
if not is_printed:
    print(-1)
