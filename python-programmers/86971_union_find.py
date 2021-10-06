# https://programmers.co.kr/learn/courses/30/lessons/86971
# union_find

from collections import defaultdict

def find_parent(node, parent):
    if parent[node] == node:
        return node
    parent[node] = find_parent(parent[node], parent)
    return parent[node]

def union(a, b, parent):
    a = find_parent(a, parent)
    b = find_parent(b, parent)
    parent[b] = a

def solution(n, wires):
    answer = n
    for i in range(n-1):
        parent = [p for p in range(n+1)]

        # union shell
        for a, b in wires[:i]:
            union(a, b, parent)
        
        for a, b in wires[i+1:]:
            union(a, b, parent)
        
        result = defaultdict(int)
        for node in range(1, n+1):
            result[find_parent(node, parent)] += 1
        cnt = list(result.values())
        if (len(cnt) == 2):
            answer = min(abs(cnt[0]-cnt[1]), answer)

    return answer