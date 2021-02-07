# todo : 효율성 높이기

import heapq
from collections import defaultdict


def solution(n, s, a, b, fares):
    INF = 100001
    ans = INF
    dist = defaultdict(lambda: INF)
    key = lambda x, y: tuple(sorted((x, y)))
    for x, y, c in fares:
        dist[key(x, y)] = c
    for i in range(1, n + 1):
        dist[(i, i)] = 0

    for _ in range(n):
        for i in range(1, n + 1):
            for j in range(i + 1, n + 1):
                for k in range(1, n + 1):
                    if j == k:
                        continue
                    dist[key(i, j)] = min(dist[key(i, j)], dist[key(i, k)] + dist[key(k, j)])

    for k in range(1, n + 1):
        ans = min(ans, dist[key(s, k)] + dist[key(k, a)] + dist[key(k, b)])
    return ans
