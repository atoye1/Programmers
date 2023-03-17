from collections import deque
# 입력 처리

row, col = map(int, input().split())
map = []
for i in range(row):
    converted = [int(c) for c in input()]
    map.append(list(converted))

# bfs을 활용한 최단거리 찾기 문제이므로 bfs를 활용한다.
# 유틸리티로 활용할 dx, dy 오프셋 배열도 미리 정한다.
# 도착위치로 이동할 수 없는 경우는 주어지지 않으므로 관련한 오류처리는 필요없다.
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(graph, start):
    q = deque()
    q.append(start)
    while q:
        c_row, c_col = q.popleft()
        for i in range(4):
            n_row = c_row + dy[i]
            n_col = c_col + dx[i]
            # 만약 범위를 벗어난 경우는 제낀다.
            if n_row < 0 or n_row >= row or n_col < 0 or n_col >= col:
                continue
            # 만약 갈 수 없는 곳이라도 제낀다.
            elif map[n_row][n_col] == 0:
                continue
            # 만약 1이라면 (한번도 방문한적이 없는 블럭이라면) 무조건 현재 노드의 값 + 1을 배정한다.
            # 깊이 우선탐색이므로 최초 방문한 경우가 무조건 최단거리가 된다.
            # 따라서 min()등으로 비교해줄 필요가 없다.
            elif map[n_row][n_col] == 1:
                map[n_row][n_col] = map[c_row][c_col] + 1
                q.append((n_row, n_col))
            # else:
            #     q.append((n_row, n_col))
            #     map[n_row][n_col] = min(
            #         map[c_row][c_col] + 1, map[n_row][n_col])


    # 결과는 여기에 출력된다.
bfs(map, (0, 0))
print(map[row-1][col-1])