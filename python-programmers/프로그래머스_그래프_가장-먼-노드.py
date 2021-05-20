def solution(n, edge):
    dist = [0 for _ in range(n + 1)]  # 거리
    graph = [[] for _ in range(n + 1)]
    visited = [False for _ in range(n + 1)]
    start = 1
    queue = [start]
    visited[start] = True

    for v1, v2 in edge:
        graph[v1].append(v2)
        graph[v2].append(v1)

    while queue:
        cur = queue.pop(0)
        next_dist = dist[cur] + 1

        for v in graph[cur]:
            if not visited[v]:
                visited[v] = True
                dist[v] = next_dist
                queue.append(v)

    max_dist = max(dist)
    return len(list(filter(lambda d: d == max_dist, dist)))


import unittest


class testCases(unittest.TestCase):
    def test(self):
        self.assertEqual(3, solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))


unittest.main()