def solution(n):
    answer = []
    def move(a, b, t, n=1):
        if n == 1:
            answer.append([a, b])
        elif n == 2:
            move(a, t, b, 1)
            move(a, b, t, 1)
            move(t, b, a, 1)
        else : 
            move(a, t, b, n-1)
            move(a, b, t)
            move(t, b, a, n-1)
    move(1, 3, 2, n)
    
    return answer