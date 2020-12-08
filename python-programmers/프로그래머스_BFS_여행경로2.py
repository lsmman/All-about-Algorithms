# 

def solution(tickets):
    visited = [False] * len(tickets)
    ans_string = ["ZZZZZ"]
    
    def dfs(tickets, cur, path, depth):
        if depth == len(tickets):
            if path < ans_string[-1]:
                ans_string[-1] = path 
            return
        for i, t in enumerate(tickets):
            if cur == t[0] and not visited[i]:
                visited[i] = True
                dfs(tickets, t[1], path+t[1] , depth + 1)
                visited[i] = False
    
    dfs(tickets, "ICN", "ICN", 0)
    answer = [ans_string[0][i:i+3] for i in range(0, len(ans_string[0]), 3)]
    return answer
