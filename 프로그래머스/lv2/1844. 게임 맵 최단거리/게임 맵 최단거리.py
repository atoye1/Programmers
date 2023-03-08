from collections import deque

def bfs(graph, start_row, start_col):
    q = deque([(start_row, start_col)]) 
    row_len = len(graph)
    col_len = len(graph[0])

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    while q:
        (x, y) = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx > row_len -1 or ny < 0 or ny > col_len - 1:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx, ny))
                
def solution(maps):
    bfs(maps, 0, 0)
    answer = maps[len(maps) - 1][len(maps[0]) - 1]
    return -1 if answer == 1 else answer
