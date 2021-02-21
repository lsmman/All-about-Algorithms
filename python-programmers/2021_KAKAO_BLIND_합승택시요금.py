from heapq import heappush, heappop

INF = 100001


def dijkstra(graph, src):
    pq = [[0, src]]
    dist = [INF for _ in range(len(graph))]
    dist[src] = 0
    while pq:
        w, x = heappop(pq)
        for y, cost in graph[x]:
            cost += w
            if dist[y] > cost:
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


""" floyd marshal - 2n^3 오래 걸림. 모든 경우가 필요할 때만 사용

def solution(n, s, a, b, fares):
    INF = int(1e9)
    ans = INF
    dist = [[INF for _ in range(n + 1)] for __ in range(n + 1)]

    for x, y, c in fares:
        dist[x][y] = dist[y][x] = c
    for i in range(1, n + 1):
        dist[i][i] = 0
    for _ in range(2):
        for i in range(1, n + 1):
            for j in range(i+1, n + 1):
                for k in range(1, n + 1):
                    c = min(dist[i][j], dist[i][k] + dist[k][j])
                    dist[i][j] = dist[j][i] = c
    for k in range(1, n + 1):
        ans = min(ans, dist[s][k] + dist[k][a] + dist[k][b])
    return ans
"""