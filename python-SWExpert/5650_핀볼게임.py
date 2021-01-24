"""
시간 : 50개 테스트케이스를 합쳐서 C의 경우 3초 / C++의 경우 3초 / Java의 경우 3초 / python의 경우 15초
메모리 : 힙, 정적 메모리 합쳐서 256MB 이내, 스택 메모리 1MB 이내

"""
# 버전 1
# 메모리 101600 KB, 실행시간 2167ms

from collections import defaultdict
import sys

sys.stdin = open("python-SWExpert\\input.txt", "r")


def get_wormhole_search(N, MAP):
    wormholes = defaultdict(list)
    wormhole_search = dict()
    for y in range(N):
        for x in range(N):
            if 6 <= MAP[y][x] and MAP[y][x] <= 10:
                wormholes[MAP[y][x]].append((x, y))
    for v in wormholes.values():
        wormhole_search[v[0]] = v[1]
        wormhole_search[v[1]] = v[0]
    return wormhole_search


def process_block_1(ball, direct):
    # 1 : left to up, right to left, up to down, down to right
    ball[2] = [2, 0, 3, 1][ball[2]]


def process_block_2(ball, direct):
    # 2 : left to down, right to left, up to right, down to up
    ball[2] = [3, 0, 1, 2][ball[2]]


def process_block_3(ball, direct):
    # 3 : left to right, right to down, up to left, down to up
    ball[2] = [1, 3, 0, 2][ball[2]]


def process_block_4(ball, direct):
    # 4 : left to right, right to up, up to down, down to left
    ball[2] = [1, 2, 3, 0][ball[2]]


def change_opposite_direction(ball, direct=None):
    # opposite direction
    ball[2] = [1, 0, 3, 2][ball[2]]


def calculate(ball, N, MAP, wormhole_search):
    score = 0
    x, y, di = (0, 1, 2)
    # left 0, right 1, up 2, down 3
    direct = ((-1, 0), (1, 0), (0, -1), (0, 1))
    start_point = ball[:2]
    do_action = {
        1: process_block_1,
        2: process_block_2,
        3: process_block_3,
        4: process_block_4,
        5: change_opposite_direction,
    }
    visit = set()
    while True:
        ball[x] = ball[x] + direct[ball[di]][x]
        ball[y] = ball[y] + direct[ball[di]][y]
        # print("x, y, di, score : ", ball[x], ball[y], ball[di], score)
        # for n in range(N):
        #     if abs(n - ball[y]) <= 2:
        #         print(n, MAP[n])
        #     if n == ball[y]:
        #         print(n, " " + " " * 3 * ball[x] + ["<", ">", "^", "v"][ball[di]])
        # print("**********************************")

        if tuple(ball) in visit:
            return -1
        visit.add(tuple(ball))

        if ball[x] < 0 or ball[x] >= N or ball[y] < 0 or ball[y] >= N:
            change_opposite_direction(ball)
            score += 1
            continue
        sign = MAP[ball[y]][ball[x]]
        if sign == -1:
            return score
        elif sign == 0:
            if start_point[x] == ball[x] and start_point[y] == ball[y]:
                return score
        elif sign <= 5:
            do_action[sign](ball, direct)
            score += 1
        else:
            ball[x], ball[y] = wormhole_search[(ball[x], ball[y])]

    return score


def solution(N, MAP):
    route_score = 0
    wormhole_search = get_wormhole_search(N, MAP)
    for y in range(N):
        for x in range(N):
            if MAP[y][x] == 0:
                for each_di in range(4):
                    score = calculate([x, y, each_di], N, MAP, wormhole_search)
                    route_score = max(route_score, score)
    return route_score


def main():
    T = int(input())
    for t in range(1, T + 1):
        N = int(input())
        MAP = [list(map(int, input().split())) for _ in range(N)]
        ans = solution(N, MAP)
        print("#{} {}".format(t, ans))


if __name__ == "__main__":
    main()
    # a = [
    #     [0, 0, 1, 0, 0, 0, 0, 3, 0, 3, 0, 0, 0, 4, 0, 0, 1, 0, 4, 0],
    #     [0, 1, 2, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 5, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 5, 0, 4, 0, 0, 0, 0],
    #     [4, 0, 0, 0, 0, 0, 0, 4, 5, 0, 0, 0, 3, 0, 0, 0, 3, 0, 0, 0],
    #     [0, 0, 0, 3, 0, 4, 1, 0, 3, 0, 0, 0, 0, 4, 0, 0, 0, 2, 0, 3],
    #     [2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 5, 0, 0, 0, 3, 4],
    #     [0, 0, 5, 0, -1, 5, 0, 0, 5, 2, 0, 0, 0, 4, 2, 0, 0, 3, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    #     [2, 0, 0, 0, 0, 3, 0, 0, 3, 3, 3, 0, 0, 1, 0, 0, 2, 0, 0, 0],
    #     [1, 5, 0, 5, 0, 0, 0, 0, 5, 4, 5, 0, 0, 0, 0, 4, 2, 4, 0, 0],
    #     [0, 4, 0, 0, 0, 1, 3, 0, 0, 0, 0, 0, 1, 0, 3, 0, 0, 2, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 3, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 3, 4, 0],
    #     [0, 4, 0, 4, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 3, 0, 0, 0, 2],
    #     [0, 5, 0, 0, 0, 4, 1, 5, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 5, 0, 0, 1, 2, 0, 0, 0, 3, 1, 2, 5, 0, 0, 0, 0, 0],
    #     [0, 4, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 4, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 1, 4, 0, 2, 0],
    #     [0, 0, 1, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 5, 0, 4, 0, 0, 0, 0, 0, 2, 0, 0, 2, 0],
    # ]
    # print(calculate([19, 8, 1], 20, a, get_wormhole_search(20, a), dict()))
    # print(solution(20, a))


# 1 9
# 2 0
# 3 7
# 4 5
# 5 19
