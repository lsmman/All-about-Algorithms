"""
시간 : 50개 테스트케이스를 합쳐서 C의 경우 30초 / C++의 경우 30초 / Java의 경우 30초 / Python의 경우 30초
메모리 : 힙, 정적 메모리 합쳐서 256MB 이내, 스택 메모리 1MB 이내

"""

import sys


def solution(K, magnatic, rotate_info):
    num_of_magnatic = 4
    rotate_info = [(r[0] - 1, r[1]) for r in rotate_info]
    top = [0] * num_of_magnatic

    def left(target, way):
        if target - 1 < 0:
            return
        side = target - 1
        left_side = (top[target] + 6 + way) % 8
        right_side = (top[side] + 2) % 8
        opp_way = -way
        if magnatic[target][left_side] != magnatic[side][right_side]:
            top[side] = (top[side] - opp_way) % 8
            left(side, opp_way)

    def right(target, way):
        if target + 1 >= 4:
            return
        side = target + 1
        left_side = (top[side] + 6) % 8
        right_side = (top[target] + 2 + way) % 8
        opp_way = -way
        if magnatic[target][right_side] != magnatic[side][left_side]:
            top[side] = (top[side] - opp_way) % 8
            right(side, opp_way)

    for cur_rotate in rotate_info:
        target, way = cur_rotate
        top[target] = (top[target] - way) % 8
        left(target, way)
        right(target, way)

    return sum([2 ** i for i in range(4) if magnatic[i][top[i]]])


def main():
    sys.stdin = open("python-SWExpert\input.txt", "r")

    T = int(input())
    for t in range(1, T + 1):
        K = int(input())
        magnatic, rotate_info = [], []
        for _ in range(4):
            magnatic.append(list(map(int, input().split())))
        for _ in range(K):
            rotate_info.append(tuple(map(int, input().split())))
        ans = solution(K, magnatic, rotate_info)
        print("#{} {}".format(t, ans))


if __name__ == "__main__":
    main()
#
# #1 10
# 2 14
# 3 3
# 4 13
# 5 15
# 6 10
# 7 2
# 8 6
# 9 5
# 10 4
