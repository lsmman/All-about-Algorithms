def solution(begin, target, words):
    answer = 0
    n = len(target)
    visited = [False] * len(words)
    stack = [[begin, 0]]
    while stack:
        string, step = stack.pop(0)
        if string is target:
            answer = step
            break
        step += 1
        for idx, word in enumerate(words):
            if visited[idx]:
                continue
                
            same_count = 0
            for i in range(n):
                if word[i] is string[i]:
                    same_count += 1
            if same_count >= n-1:
                stack.append([word, step])
                visited[idx] = True
                    
    return answer