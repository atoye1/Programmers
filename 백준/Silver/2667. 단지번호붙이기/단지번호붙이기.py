from collections import deque

size = int(input())
board = [list(map(int, list(input()))) for _ in range(size)]
moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def bfs(board, start):
    q = deque()
    q.append(start)
    count = 1
    while q:
        r, c = q.popleft()
        board[r][c] = -1  # 방문표시를 해준다.
        for move in moves:
            nr, nc = r + move[0], c + move[1]
            # 인덱스를 벗어나면 넘겨준다.
            if nr < 0 or nc < 0 or nr >= size or nc >= size:
                continue
            elif board[nr][nc] == 1:  # 집이 있으면
                board[nr][nc] = -1  # -1로 방문표시를 해준다.
                q.appendleft((nr, nc))  # 큐에 삽입해주고
                count += 1  # 카운트를 하나 증가시킨다.
    return count


result = []  # 결과를 저장할 배열을 미리 선언한다.
for i in range(size):
    for j in range(size):
        # 만약 현재 블럭이 1이면 단지가 시작한 것이다.
        if board[i][j] == 1:
            count = bfs(board, (i, j))
            result.append(count)
result.sort()
print(len(result))
for num in result:
    print(num)
