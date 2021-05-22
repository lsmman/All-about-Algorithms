def solution(n, costs):
    costs.sort(key=lambda x: x[2])
    connected = [set() for _ in range(n)]
    result = 0
    
    def is_connected(x, y):
        visited = [False] * (n+1)
        visited[x]
        queue = [x]
        while queue:
            cur = queue.pop(0)
            for c in connected[cur]:
                if not visited[c]:
                    visited[c] = True
                    if c == y:
                        return True
                    queue.append(c)
                    
        return False

    for x, y, cost in costs:
        if not is_connected(x, y):
            connected[x].add(y)
            connected[y].add(x)
            result += cost
    return result

