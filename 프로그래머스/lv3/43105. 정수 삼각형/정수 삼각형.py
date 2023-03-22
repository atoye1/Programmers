def solution(tri):
    n = len(tri)
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

    answer = max(tri[-1])

    return answer