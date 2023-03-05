N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]


def getMin(row, col):
    wrong_white = 0
    wrong_black = 0
    # (0, 0) == 'W' 인 경우
    for row_idx in range(row, row + 8):
        for col_idx in range(col, col + 8):
            if (row_idx + col_idx) % 2 == 0 and board[row_idx][col_idx] != 'W':
                wrong_white += 1
            elif (row_idx + col_idx) % 2 != 0 and board[row_idx][col_idx] != 'B':
                wrong_white += 1
    # (0, 0) == 'B' 인 경우
    for row_idx in range(row, row + 8):
        for col_idx in range(col, col + 8):
            if (row_idx + col_idx) % 2 == 0 and board[row_idx][col_idx] != 'B':
                wrong_black += 1
            elif (row_idx + col_idx) % 2 != 0 and board[row_idx][col_idx] != 'W':
                wrong_black += 1

    return min(wrong_black, wrong_white)


minBlock = N * M
for row in range(N - 8 + 1):
    for col in range(M - 8 + 1):
        minBlock = min(minBlock, getMin(row, col))

print(minBlock)
