def solution(m, n, puddles):
    # m * n을 행렬로 표현하면 n행, m열이다.
    # 인덱스가 0부터 시작하므로 board[0][0] 에서 board[n - 1][m - 1]로 가는 경우를 찾아야 한다.
    # 이동하는 방향은 옆으로 가거나 아래로 간다.
    # 다이나믹 프로그래밍적 요소는 해당 지점까지 도착하는 모든 경우의 수는 바로 윗지점에 가는 경우의 수 + 바로 왼쪽지점 경우의 수 이다.
    # 점화식은 아래와 같이 나온다.
    # dist[a][b] = dist[a - 1][b] + dist[a][b - 1]
    # 이 점화식을 바탕으로 풀어나가면 되는데 고려할 사항은 물이 있는 칸이다.
    # 물이 있는 칸은 -1로 표현해준다.
    
    #n 행 m열인 2차원 배열을 생성한다.
    board = [[0 for _ in range(m)] for _ in range(n)]
    # 초기 지점은 1로 초기화해준다.
    board[0][0] = 1
    for puddle in puddles:
        col, row = puddle
        # row, col에 -1씩 해줘야 맞다. 내가 활용중인 보드는 (0,0)에서 시작하기 때문이다.
        board[row - 1][col - 1] = -1 # 물은 -1로 표시한다.
        
    for row in range(n):
        for col in range(m):
            # 값이 아직 없는 장소라면
            if board[row][col] == 0:
                # 위의 블럭을 체크한다. 인덱스가 유효하고 물이 없어야 한다.
                n_row, n_col = row - 1, col
                if n_row >= 0 and board[n_row][n_col] != -1:
                    board[row][col] += board[n_row][n_col]

                # 왼쪽 블럭을 체크한다. 역시 인덱스가 유효하고 물이 없어야 한다.
                n_row, n_col = row, col - 1
                if n_col >= 0 and board[n_row][n_col] != -1:
                    board[row][col] += board[n_row][n_col]
            
    return board[n - 1][m - 1] % 1000000007