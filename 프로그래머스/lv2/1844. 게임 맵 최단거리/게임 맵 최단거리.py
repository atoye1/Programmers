from collections import deque
# 최단거리 찾기 문제는 bfs를 이용한다고 했다.
# 너비우선탐색으로 해당 칸에 도착하는데 필요한 가장 짧은 거리를 계산하고 기록한다
# n, m 모두 100 이하의 자연수이므로 완전탐색방식인 bfs를 사용할 수 있다.
def solution(maps):
    #maps 2차원 배열을 대상으로 bfs를 하면서 기록하고, 마지막에 값을 돌려주면 된다.
    bfs(maps, (0, 0))
    answer = maps[len(maps) - 1][len(maps[0]) - 1]
    answer = -1 if answer == 1 else answer
    return answer

def bfs(maps, start):
    
    s_row, s_col = start
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    
    q = deque()
    q.append((s_row, s_col))
    visited = [[False for _ in range(len(maps[0]))] for _ in range(len(maps))]
    while q:
        row, col = q.popleft()
        now_count = maps[row][col]
        for i in range(4):
            n_row, n_col = row + dy[i], col + dx[i]
            if n_row < 0 or n_row > len(maps) - 1 or n_col < 0 or n_col > len(maps[0]) - 1:
                continue
            if visited[n_row][n_col]:
                continue
            if maps[n_row][n_col] == 0:
                continue
            maps[n_row][n_col] = now_count + 1
            q.append((n_row, n_col))
            visited[n_row][n_col] = True
    return maps
