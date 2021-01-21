"""
시간 : 50개 테스트케이스를 합쳐서 C의 경우 3초 / C++의 경우 3초 / Java의 경우 3초 / python의 경우 15초
메모리 : 힙, 정적 메모리 합쳐서 256MB 이내, 스택 메모리 1MB 이내

"""

import sys
from collections import defaultdict


def get_wormhole_search(N, MAP):
    wormholes = defaultdict(list)
    # blackhole_exist = False
    for y in range(N):
        for x in range(N):
            # if MAP[x][y] == -1:
            #     blackhole_exist = True
            if 6 <= MAP[x][y] and MAP[x][y] <= 10:
                wormholes[MAP[x][y]].append((x, y))
    wormhole_search = dict()
    for v in wormholes.values():
        wormhole_search[v[0]] = v[1]
        wormhole_search[v[1]] = v[0]
    # return (blackhole_exist, wormhole_search)
    return wormhole_search
    
def process_block_1(ball):
    # 1 : left to up, right to left, up to down, down to right
    change_direction = [2, 0, 3, 1]
    ball[2] = change_direction[ball[2]]

def process_block_2(ball):
    # 2 : left to down, right to left, up to right, down to up
    change_direction = [3, 0, 1, 2]
    ball[2] = change_direction[ball[2]]

def process_block_3(ball):
    # 3 : left to right, right to down, up to left, down to up
    change_direction = [1, 3, 0, 2]
    ball[2] = change_direction[ball[2]]

def process_block_4(ball):
    # 4 : left to right, right to up, up to down, down to left
    change_direction = [1, 2, 3, 0]
    ball[2] = change_direction[ball[2]]

def change_opposite_direction(ball):
    # opposite direction
    change_direction = [1, 0, 3, 2]
    ball[2] = change_direction[ball[2]]
    
def solution(N, MAP):
    # 점수 visit 만들기
    
    wormhole_search = get_wormhole_search(N, MAP)
    ball = [0, 0, 1] # start
    score = calculate(ball, N, MAP, wormhole_search)

    return 0

def calculate(ball, N, MAP, wormhole_search):
    # 종료 조건 만들기
    # visit 만들기
    
    score = 0
    x, y, di = (0, 1, 2)
    # left 0, right 1, up 2, down 3
    direct = ((-1, 0), (1, 0), (0, -1), (0,1))
    do_action = {1:process_block_1, 2:process_block_2, 3:process_block_3, 4:process_block_4, 5:change_opposite_direction}

    while True:        
        new_x = ball[x] + direct[ball[di]][x]
        new_y = ball[y] + direct[ball[di]][y]
        if new_x < 0 or new_x >= N or new_y < 0 or new_y >= N:
            change_opposite_direction(ball)
            score += 1
        else:
            sign = MAP[new_x][new_y]
            if sign == -1:
                return score
            elif sign <= 5:
                do_action[sign](ball)
                score += 1
            else:
                new_x, new_y = wormhole_search[(new_x, new_y)]
        ball[x], ball[y] = new_x, new_y
                
    return score


def main():
    sys.stdin = open("python-SWExpert\\input.txt", "r")

    T = int(input())
    for t in range(1, T + 1):
        N = int(input())
        MAP = [list(map(int, input().split())) for _ in range(N)]
        ans = solution(N, MAP)
        print("#{} {}".format(t, ans))


if __name__ == "__main__":
    # main()
    


# 1 9
# 2 0
# 3 7
# 4 5
# 5 19
