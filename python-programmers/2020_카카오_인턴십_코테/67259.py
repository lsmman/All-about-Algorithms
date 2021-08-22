# 경주로 건설
# https://programmers.co.kr/learn/courses/30/lessons/67259?language=python3


def solution(board):
    answer = 0
    return answer

result = solution([[0,0,0],[0,0,0],[0,0,0]])
print(result == 900, result)
result = solution([[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]])
print(result == 3800, result)
result = solution([[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]])
print(result == 2100, result)
result = solution([[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]])
print(result == 3200, result)