import sys
from collections import deque

input = sys.stdin.readline
# 입력
N, M, K, X = map(int, input().split())
roads = [[] for _ in range(N + 1)]
for _ in range(M):
    x, y = map(int, input().split())
    roads[x].append(y)

# 변수 정의
visited = [-1 for _ in range(N + 1)]
# 알고리즘 결정
# 너비우선탐색


def bfs(x):
    q = deque()
    q.append(x)
    visited[x] = 0
    answer = []
    while q:
        x = q.popleft()
        for y in roads[x]:
            if visited[y] == -1:
                q.append(y)
                visited[y] = visited[x] + 1
                if visited[y] == K:
                    answer.append(y)
    if len(answer) == 0:
        print(-1)
    else:
        answer.sort()
        for answer in answer:
            print(answer, end=' ')


bfs(X)
