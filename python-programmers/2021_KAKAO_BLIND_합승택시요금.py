from heapq import heappush, heappop

INF = int(1e9)

# 2|V|n
def dijkstra(graph, src):
    pq = [[0, src]]
    dist = [INF for _ in range(len(graph))]
    dist[src] = 0
    while pq:
        w, x = heappop(pq)
        if dist[x] < w:
            continue
        for y, cost in graph[x]:
            cost += w
            if cost < dist[y]:
                dist[y] = cost
                heappush(pq, [cost, y])
    return dist


def solution(n, s, a, b, fares):
    graph = [[] for _ in range(n + 1)]
    ans = INF
    for src, dst, cost in fares:
        graph[src].append((dst, cost))
        graph[dst].append((src, cost))
    for k in range(1, n + 1):
        dist_k = dijkstra(graph, k)
        ans = min(ans, dist_k[s] + dist_k[a] + dist_k[b])
    return ans


""" floyd marshal - n^3 오래 걸림. 모든 경우가 필요할 때만 사용
from itertools import product

def solution(n, s, a, b, fares):
    INF = int(1e9)
    ans = INF
    dist = [[INF for _ in range(n + 1)] for __ in range(n + 1)]

    for x, y, c in fares:
        dist[x][y] = dist[y][x] = c
    for i in range(1, n + 1):
        dist[i][i] = 0
    for k, i, j in product(range(1, n+1), repeat=3):
        dist[i][j] = dist[j][i] = min(dist[i][j], dist[i][k] + dist[k][j])
    for k in range(1, n + 1):
        ans = min(ans, dist[s][k] + dist[k][a] + dist[k][b])
    return ans

"""