# 자리정하기
# N * N의 행렬이다.
# N의 최대 크기는 20이므로 완전탐색해도 된다.
'''


'''
n = int(input())
orders = [list(map(int, input().split()))
          for _ in range(n ** 2)]
board = [[0] * n for _ in range(n)]
search_pos = [(1, 0), (-1, 0), (0, 1), (0, -1)]
likes_to_point = [0, 1, 10, 100, 1000]


def get_position(board, order):
    # 좋아하는 학생이 0, 1, 2, 3, 4까지 있을 수 있음
    max_likes = 0
    candidates = []
    for row in range(n):
        for col in range(n):
            if board[row][col] != 0:  # 이미 앉은 학생이 있으면 넘어간다.
                continue
            # 현재 좌표에서 상하좌우를 돌면서 좋아하는 학생이 있는지 찾는다.
            curr_likes = 0
            for pos in search_pos:
                n_row = row + pos[0]
                n_col = col + pos[1]
                if n_row < 0 or n_col < 0 or n_row >= n or n_col >= n:
                    continue
                if board[n_row][n_col] in order[1:]:
                    curr_likes += 1
            # row, col의 likes를 계산한 다음, 저장된 최적값이랑 같은 경우는 candidates에 append하고,
            # 저장된 최적값보다 크면 candidate를 비워야 한다.
            if curr_likes == max_likes:
                candidates.append((row, col))
            elif curr_likes > max_likes:
                max_likes = curr_likes
                candidates = [(row, col)]
    if len(candidates) == 1:
        return candidates[0]
    else:
        max_empty = 0
        result = candidates[0]
        for row, col in candidates:
            curr_empty = 0
            for pos in search_pos:
                n_row = row + pos[0]
                n_col = col + pos[1]
                if n_row < 0 or n_col < 0 or n_row >= n or n_col >= n:
                    continue
                if board[n_row][n_col] == 0:
                    curr_empty += 1
            if curr_empty > max_empty:
                max_empty = curr_empty
                result = (row, col)
        return result


def get_point(board, orders):
    total = 0
    for row in range(n):
        for col in range(n):
            curr_student = board[row][col]  # 현재 학생의 번호
            curr_liking = [
                order for order in orders if order[0] == curr_student]
            likes = 0
            for pos in search_pos:
                n_row = row + pos[0]
                n_col = col + pos[1]
                if n_row < 0 or n_col < 0 or n_row >= n or n_col >= n:
                    continue
                # 현재 학생이 좋아하는 학생인 경우 like를 증가시킨다:
                if board[n_row][n_col] in curr_liking[0]:
                    likes += 1
            total += likes_to_point[likes]
    return total


for order in orders:
    row, col = get_position(board, order)
    board[row][col] = order[0]

print(get_point(board, orders))
