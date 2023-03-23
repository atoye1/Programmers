from collections import deque

# 시간을 줄이기 위해 stdin.readline활용한다.
import sys
input = sys.stdin.readline


# 모듈화해서 개발하니 디버깅이 훨씬 쉬웠다.
# is_ripen 함수를 잘못 작성했었는데 모듈화를 해서 틀린점을 쉽게 찾을 수 있었다.
# n^2시간에 체크하는 is_ripen을 사용했더니 시간초과가 떠서
# count변수를 제거해가면서 전부다 익었는지 여부를 체크하도록 변경
def count_zero(board):
    count = 0
    for i in board:
        for j in i:
            if j == 0:  # 만약 0인 토마토가 한개라도 있으면 전부다 익지 않은 것이다.
                count += 1
    return count


# 입력 값 처리
col, row = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(row)]

time = 0
q = deque()
for i in range(len(board)):
    for j in range(len(board[0])):
        if board[i][j] == 1:
            q.append((i, j, time))
count = count_zero(board)
# 네 방향으로 전염되는걸 배열에 담았다.
moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
# bfs이므로 뎈을 활용한다.
while q:
    if count == 0:
        break
    r, c, time = q.popleft()
    # 현재 토마토가 익어있으면
    if board[r][c] == 1:
        # 4가지 방향으로 탐색한다.
        for move in moves:
            nr, nc, nt = r + move[0], c + move[1], time + 1
            # 인덱스 체크를 해서 적절한 경우만.
            if nr >= 0 and nr < row and nc >= 0 and nc < col:
                if board[nr][nc] == 0:  # 덜익은 토마토인 경우만.
                    board[nr][nc] = 1  # 익히고
                    q.append((nr, nc, nt))  # 다음 전염을 위해 옮겨준다.
                    count -= 1  # 카운트를 감소시킨다.
    time += 1

if count == 0:
    print(time)
else:
    print(-1)
