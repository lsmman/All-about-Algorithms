# 2021 카카오 채용연계 인턴쉽

from itertools import product

def solution(places):
    answer = [1] * len(places)
    P, X, O = ["P", "X", "O"]
    size = 5
    
    is_valid = lambda p: 0 <= p < size
    
    for i, place in enumerate(places):
        y, x = 0, 0
        for y, x in product(range(5), repeat=2):
            pos = place[y][x]
            if pos != P:
                continue

            # 오른쪽으로 1칸
            if is_valid(x+1) and place[y][x+1] == P:
                answer[i] = 0
                break

            # 오른쪽으로 2칸
            if (
                is_valid(x+2) and 
                place[y][x+2] == P and 
                place[y][x+1] != X
            ):
                answer[i] = 0
                break

            # 아래로 1칸
            if is_valid(y+1) and place[y+1][x] == P:
                answer[i] = 0
                break

            # 아래로 2칸
            if (
                is_valid(y+2) and 
                place[y+2][x] == P and 
                place[y+1][x] != X
            ):
                answer[i] = 0
                break

            # 아래 오른쪽 대각선 
            if (
                is_valid(x+1) and
                is_valid(y+1) and
                place[y+1][x+1] == P and
                (
                    place[y+1][x] != X or
                    place[y][x+1] != X
                )
            ):
                answer[i] = 0
                break

            # 아래 왼쪽 대각선 
            if (
                is_valid(x-1) and
                is_valid(y+1) and
                place[y+1][x-1] == P and
                (
                    place[y+1][x] != X or
                    place[y][x-1] != X
                )
            ):
                answer[i] = 0
                break

    return answer