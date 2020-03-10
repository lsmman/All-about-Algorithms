# 숫자만 카운트한 버전

def BFS(node, visited, computers):
    stack = [node]
    while stack:
        target = stack.pop()
        for idx, conn in enumerate(computers[target]):
            if conn and not visited[idx]:
                stack.append(idx)
                visited[idx] = True
            
def solution(n, computers):
    answer = 0
    visited = [False] * n
    for node in range(n):
        if not visited[node]:
            answer += 1
            BFS(node, visited, computers)
    return answer



