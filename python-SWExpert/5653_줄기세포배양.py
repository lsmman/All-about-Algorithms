"""
시간 : 50개 테스트케이스를 합쳐서 C의 경우 3초 / C++의 경우 3초 / Java의 경우 3초 / Python의 경우 15초
메모리 : 힙, 정적 메모리 합쳐서 256MB 이내, 스택 메모리 1MB 이내

"""

import sys
from collections import deque


def spread(cur_info, whole_map, new_cells, limit_x, limit_y):
    x, y, life = cur_info
    inactive, empty = 1, 0
    for add_x, add_y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        new_x, new_y = x + add_x, y + add_y
        if (
            new_x >= 0
            and new_x < limit_x
            and new_y >= 0
            and new_y < limit_y
            and (
                whole_map[new_x][new_y][0] == empty
                or ((new_x, new_y) in new_cells and whole_map[new_x][new_y][2] < life)
            )
        ):
            whole_map[new_x][new_y] = [inactive, life, life]
            new_cells.append((new_x, new_y))
    return


def solution(N, M, K, matrix):
    answer = t = 0
    queue = deque()
    inactive, active, dead, empty = (1, 2, -1, 0)  # 비활성, 활성, 죽음, 원래부터 없음
    status, remain, _life = (0, 1, 2)
    spread_leng = 150
    limit_x, limit_y = N + spread_leng * 2, M + spread_leng * 2
    whole_map = [[[empty, 0, 0] for _ in range(limit_y)] for __ in range(limit_x)]
    # [status, remain, life] : 현재 상태, 상태의 남은 생명력, 생명력 수치

    for i in range(N):
        for j in range(M):
            if matrix[i][j]:  # 생명력이 있으면
                whole_map[spread_leng + i][spread_leng + j] = [inactive, matrix[i][j], matrix[i][j]]
                queue.append((spread_leng + i, spread_leng + j))
    while queue and t < K:
        new_cells = []
        for _ in range(len(queue)):
            cur_x, cur_y = queue.popleft()
            cur_status, cur_remain, cur_life = whole_map[cur_x][cur_y]
            if cur_status == inactive:
                if cur_remain == 1:
                    whole_map[cur_x][cur_y][status] = active
                    whole_map[cur_x][cur_y][remain] = cur_life
                else:
                    whole_map[cur_x][cur_y][remain] -= 1
            elif cur_status == active:
                spread((cur_x, cur_y, cur_life), whole_map, new_cells, limit_x, limit_y)
                if cur_remain == 1:
                    whole_map[cur_x][cur_y][status] = dead
                else:
                    whole_map[cur_x][cur_y][remain] -= 1
            if cur_status >= 1:
                queue.append((cur_x, cur_y))
        queue.extend(new_cells)
        t += 1

    for i in range(limit_x):
        for j in range(limit_y):
            if whole_map[i][j][status] >= 1:
                answer += 1
    return answer


def main():
    sys.stdin = open("python-SWExpert\input.txt", "r")

    T = int(input())
    for t in range(1, T + 1):
        matrix = []
        N, M, K = map(int, input().split())
        for _ in range(N):
            matrix.append(list(map(int, input().split())))
        ans = solution(N, M, K, matrix)
        print("#{} {}".format(t, ans))


if __name__ == "__main__":
    main()

    # test 1
    # solution(2, 2, 10, [[1, 1], [0, 2]])
    # test 2
    # print(
    #     solution(
    #         5,
    #         5,
    #         19,
    #         [[3, 2, 0, 3, 0], [0, 3, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 2]],
    #     )
    # )

# def print_method_queue_and_whole_map_by_status():
# print("---- #", t, len(queue))
# term = 9
# for r in whole_map[150 - term : 150 + term + N]:
#     for c in r[150 - term : 150 + term + M]:
#         mark = c[0]
#         if c[0] == inactive:
#             mark = "i" + str(c[1]) + str(c[2])
#         elif c[0] == active:
#             mark = "a" + str(c[1]) + str(c[2])
#         elif c[0] == dead:
#             mark = "d" + "00"
#         else:
#             mark = "000"
#         print(mark, end=" ")
#     print()

"""
#1 22
#2 36
#3 90
#4 164
#5 712
"""