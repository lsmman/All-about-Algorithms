# 2021 카카오 채용연계 인턴쉽
# 82점

from collections import defaultdict
import heapq


def solution(n, start, end, roads, traps):
    answer = 2147483647
    sample_key = tuple([False] * len(traps))
    node_edges = [set() for _ in range(n+1)]
    edges = {}
    traps_set = set(traps)
    dp = defaultdict(lambda:2147483647)
    
    isTrap = lambda x: x in traps_set
    
    def get_edge_info(a, b, key):
        val, direction = edges[(a, b)]
        a_is_trap = False
        b_is_trap = False
        
        if isTrap(a):
            a_is_trap = key[traps.index(a)]
        if isTrap(b):
            b_is_trap = key[traps.index(b)]
        
        can_move = direction ^ (a_is_trap ^ b_is_trap)
        
        return val, can_move
    
    
    for a, b, val in roads:
        node_edges[a].add(b)
        node_edges[b].add(a)
        edges[(a, b)] = [val, True]
        edges[(b, a)] = [val, False]
    
    queue = [(0, start, sample_key)]
    heapq.heapify(queue)
    
    while queue:
        move, cur, cur_key = heapq.heappop(queue)
        if answer <= move:
            continue

        if cur == end:
            answer = min(answer, move)
            continue

        if isTrap(cur):
            trap_index = traps.index(cur)
            cur_key = list(cur_key)
            cur_key[trap_index] = not cur_key[trap_index]
            cur_key = tuple(cur_key)
            
        for node in node_edges[cur]:
            val, is_valid = get_edge_info(cur, node, cur_key)
            if not is_valid:
                continue
                
            if dp[(node, cur, val, cur_key)] <= move + val:
                continue
            
            dp[(node, cur, val, cur_key)] = move + val
            heapq.heappush(queue, (move+val, node, tuple(cur_key[:])))
        
    return answer