from collections import defaultdict
from copy import deepcopy


def solution(tickets):
    def find_next(route, cur, remain):
        if not remain:
            return [cur]
        for r in route[cur]:
            temp_route = deepcopy(route)
            temp_route[cur].remove(r)
            result = find_next(temp_route, r, remain - 1)
            if result:
                return [cur] + result
        return []

    route = defaultdict(list)
    for d, a in tickets:
        route[d].append(a)
    for l in route.values():
        l.sort()
    result = find_next(route, "ICN", len(tickets))
    return result