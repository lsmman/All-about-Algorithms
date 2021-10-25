
import sys
from collections import deque


def solve(n, graph):
    def bfs(node):
        visited = [False] * (n + 1)
        visited[node] = True
        dq = deque([node])
        cnt = 1
        while dq:
            cur = dq.popleft()
            for g in graph[cur]:
                if visited[g]:
                    continue
                dq.append(g)
                visited[g] = True
                cnt += 1

        return cnt

    visit_cnt = [0]
    for i in range(1, n+1):
        visit_cnt.append(bfs(i))

    max_cnt = max(visit_cnt)
    answer = ""
    for i, c in enumerate(visit_cnt):
        if c == max_cnt:
            answer += str(i) + " "
    return answer


def main():
    n, m = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        graph[b].append(a)
    result = solve(n, graph)
    print(result)


main()


# def test():
#     answer = "1 2 "
#     result = solve(5, 4, [[3, 1], [3, 2], [4, 3], [5, 3]])
#     print(result, result == answer)
#
#     answer = "1 2 3 6 "
#     result = solve(6, 5, [[1, 2], [2, 3], [3, 1], [4, 5], [5, 6]])
#     print(result, result == answer)



# 3 <- 1
# 3 <- 2
# 4 <- 3
# 5 <- 3
#
# 1 2
#
# 1
# |    2
# v  /
# 3   ->    4
#   \
#     5