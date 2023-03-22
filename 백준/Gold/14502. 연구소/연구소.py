from itertools import combinations
from collections import deque


def bfs(graph, start):
    moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    q = deque()
    q.append(start)
    while q:
        r, c = q.popleft()
        # 4가지 방향에 대해서 new_row, new_col을 정의해야 한다.
        for move in moves:
            nr, nc = r + move[0], c + move[1]
            # 먼저 nr, nc가 유효한 좌표인지 확인한다.
            # 좌표가 유효하지 않다면 넘긴다.
            if nr < 0 or nr > row - 1 or nc < 0 or nc > col - 1:
                continue
            if graph[nr][nc] == 0:  # 만약 새로운 좌표가 감염가능한 안전영역이면,
                graph[nr][nc] = 2  # 감염시킨다.
                q.append((nr, nc))
            else:
                continue


row, col = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(row)]

empty_coords = []
for r in range(row):
    for c in range(col):
        if board[r][c] == 0:
            empty_coords.append((r, c))
cases = combinations(empty_coords, 3)

answer = 0
for case in cases:
    # 이번 케이스에서 쓸 보드를 만든다.
    new_board = [[] for _ in range(row)]
    viruses = []
    safe_count = 0  # 안전영역 카운트를 초기화 한
    # 뉴 보드를 원본과 동기화시키면서 벽을 세울 장소는 따로 지정해준다.
    for i in range(row):
        for j in range(col):
            if (i, j) in case:
                new_board[i].append(1)
            else:
                new_board[i].append(board[i][j])
                if board[i][j] == 2:
                    viruses.append((i, j))
    # 뉴 보드를 대상으로 너비우선탐색을 진행한다.
    # 시작점은 바이러스의 위치이므로 viruses배열을 반복문으로 돌면서 bfs탐색한다.
    while viruses:
        r, c = viruses.pop()
        bfs(new_board, (r, c))
    # 보드에 감염 가능한 모든 감염이 처리되었으므로 안전영역을 카운트 해야 한다.
    for r in range(row):
        for c in range(col):
            if new_board[r][c] == 0:
                safe_count += 1
    answer = max(answer, safe_count)

print(answer)

# print(len(list(cases)))
