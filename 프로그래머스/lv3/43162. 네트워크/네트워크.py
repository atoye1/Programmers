def dfs(graph, start, visited):
    stack = [start]
    
    while stack:
        curr = stack.pop()
        if curr not in visited:
            visited.append(curr)
            for idx, i in enumerate(graph[curr]):
                if i == 1:
                    stack.append(idx)
    
def solution(n, computers):
    visited = []
    count = 0
    for i in range(n):
        if i not in visited:
            dfs(computers, i, visited)
            count += 1
    print(visited)
    return count