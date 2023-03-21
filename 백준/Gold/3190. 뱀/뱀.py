from collections import deque
size = int(input())

apple_count = int(input())
apples = []
for _ in range(apple_count):  # 사과 위치를 배열에 저장한다.
    row, col = map(int, input().split())
    apples.append((row, col))

direction_count = int(input())
directions = []
for _ in range(direction_count):  # 이미 시간순으로 정렬되어 있다.
    time, direction = input().split()
    directions.append((int(time), direction))

# 보드를 초기화 한다.
board = [[0] * size for _ in range(size)]
# 사과가 있는 위치를 보드에 표시해놓는다.
# 1,1부터 시작이므로 보드에 표시하려면 row, col 모두 -1한 상태에서 표시해야한다.
# 사과가 있으면 1, 사과가 없으면 0으로 마킹한다.
for apple in apples:
    board[apple[0] - 1][apple[1] - 1] = 1

# 이제 0,0 부터 시뮬레이션을 수행한다.
# 스네이크라는 데이터는 어떤 자료구조에 들어갈까? 큐? 리스트? 셋?
# 종료조건 즉, 게임이 끝나는 조건은 뭘까?
# - 스네이크가 벽에 머리를 박는다.
# - 스네이크가 자기자신에 머리를 박는다.
# 스네이크의 움직이는 방향이 4가지 경우가 있다.
snake = deque([[0, 0]])
# !!!move에서 down을 잘못 정해줘서 디버깅했다!!!
move = [[0, 1], [1, 0], [0, -1], [-1, 0]]  # 나머지 연산자 사용하기위해서 배열로 변경했다.
curr_move = 0
time = 0
while True:
    # 일단 뱀은 움직인다. 방향에 따라서. 초기에는 Right로 움직인다.
    # 새로운 헤드는 현재 헤드에다가 해당하는 move의 값을 더해준 값이다.
    time += 1
    nr, nc = snake[0][0] + move[curr_move][0], snake[0][1] + move[curr_move][1]
    if nr < 0 or nr >= size or nc < 0 or nc >= size:
        # 만약 현재 헤드의 위치가 부적절하면 게임이 종료된다.
        break
    if [nr, nc] in snake:  # 만약 새로운 헤드가 자신과 부딪히면 겜이 종료된다.
        break

    # 여기서 부터는 이동한 결과가 적절했단 의미이므로, 사과를 봐야한다.
    # 일단 새로운 헤드를 스네이크 뎈에 넣는다
    snake.appendleft([nr, nc])
    if board[nr][nc] != 1:  # 사과가 없으면 꼬리칸을 비워준다.
        snake.pop()
    else:  # 사과랑 만나면 사과를 먹는다.
        board[nr][nc] = 0
    # 시간이 증가하면 방향전환이 있는지 살펴봐야 한다.
    # directions 배열이 비워졌을 때를 대비해서 조건을 하나 더 추가한다.
    if directions and directions[0][0] == time:
        _, rotation = directions.pop(0)
        # 'D'인경우 오른쪽 회전이므로 인덱스가 올라간다.
        curr_move = curr_move + 1 if rotation == 'D' else curr_move - 1
        curr_move %= 4  # 나머지연산자를 활용해서 배열의 인덱스로 바꿔준다.
print(time)
