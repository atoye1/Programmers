from collections import deque
# 최단거리 찾기 문제는 bfs를 이용한다고 했다.
# 너비우선탐색으로 해당 칸에 도착하는데 필요한 가장 짧은 거리를 계산하고 기록한다
# n, m 모두 100 이하의 자연수이므로 완전탐색방식인 bfs를 사용할 수 있다.
def solution(maps):
    #maps 2차원 배열을 대상으로 bfs를 하면서 기록하고, 마지막에 값을 돌려주면 된다.
    bfs(maps, (0, 0))
    answer = maps[len(maps) - 1][len(maps[0]) - 1]
    # 만약 answer가 그대로 1이라면 도달하지 못한 것
    answer = -1 if answer == 1 else answer
    return answer

def bfs(maps, start):
    
    s_row, s_col = start
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    
    q = deque()
    q.append((s_row, s_col))
    # visited를 O(N)시간에 접근하도록 작성하면 시간초과가 나온다.
    #visited = [[False for _ in range(len(maps[0]))] for _ in range(len(maps))]
    
    while q:
        row, col = q.popleft()
        now_count = maps[row][col]
        for i in range(4):
            n_row, n_col = row + dy[i], col + dx[i]
            # 인덱스가 범위를 벗어난 경우 처리
            if n_row < 0 or n_row > len(maps) - 1 or n_col < 0 or n_col > len(maps[0]) - 1:
                continue
            # 이미 방문한 경우 처리
            #if visited[n_row][n_col]:
            #    continue
            # 갈수 없는 곳인 경우 처리
            if maps[n_row][n_col] == 0 or maps[n_row][n_col] != 1:
                continue
            # 지금의 블록에 인접해 있으므로 +1 해준다.
            maps[n_row][n_col] = now_count + 1
            q.append((n_row, n_col))
            #visited[n_row][n_col] = True
    return maps
