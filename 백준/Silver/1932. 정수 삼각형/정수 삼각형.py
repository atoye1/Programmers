n = int(input())
tri = [list(map(int, input().split())) for _ in range(n)]

# 삼각형의 2번째 줄부터 시작한다.
# 첫번째 줄은 원소가 하나이기 때문이다.
# 현재 줄에서 닿을 수 있는 위쪽 원소를 프로그래밍적으로 구현하는게 핵심이다.
for i in range(1, n):
    for j in range(len(tri[i])):
        # 만약 첫번째 원소면 윗줄의 첫번째 원소만 덧셈 가능
        if j == 0:
            tri[i][j] += tri[i - 1][0]
        # 만약 마지막 원소면 윗줄의 마지막원소만 더할수 있다.
        elif j == len(tri[i]) - 1:
            tri[i][j] += tri[i - 1][-1]
        else:  # 중간에 있는 원소면 윗줄의 자기 인덱스 - 1 또는 자기인덱스인 원소를 더할 수 있다.
            tri[i][j] += max(tri[i - 1][j - 1], tri[i - 1][j])

print(max(tri[-1]))
