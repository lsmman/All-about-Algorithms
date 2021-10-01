"""
비바라기를 시전하면 (N, 1), (N, 2), (N-1, 1), (N-1, 2)에 비구름이 생긴다. 
구름은 칸 전체를 차지한다. 이제 구름에 이동을 M번 명령하려고 한다. 
i번째 이동 명령은 방향 di과 거리 si로 이루어져 있다. 방향은 총 8개의 방향이 있으며,
 8개의 정수로 표현한다. 1부터 순서대로 ←, ↖, ↑, ↗, →, ↘, ↓, ↙ 이다. 이동을 명령하면 다음이 순서대로 진행된다.

1. 모든 구름이 di 방향으로 si칸 이동한다.
2. 각 구름에서 비가 내려 구름이 있는 칸의 바구니에 저장된 물의 양이 1 증가한다.
3. 구름이 모두 사라진다.
4. 2에서 물이 증가한 칸 (r, c)에 물복사버그 마법을 시전한다. 물복사버그 마법을 사용하면, 
    대각선 방향으로 거리가 1인 칸에 물이 있는 바구니의 수만큼 (r, c)에 있는 바구니의 물이 양이 증가한다.
    이때는 이동과 다르게 경계를 넘어가는 칸은 대각선 방향으로 거리가 1인 칸이 아니다.
    예를 들어, (N, 2)에서 인접한 대각선 칸은 (N-1, 1), (N-1, 3)이고, (N, N)에서 인접한 대각선 칸은 (N-1, N-1)뿐이다.
5. 바구니에 저장된 물의 양이 2 이상인 모든 칸에 구름이 생기고, 물의 양이 2 줄어든다. 
    이때 구름이 생기는 칸은 3에서 구름이 사라진 칸이 아니어야 한다.

M번의 이동이 모두 끝난 후 바구니에 들어있는 물의 양의 합을 구해보자.
"""
from copy import deepcopy

# direct2xy : 순서대로 ←, ↖, ↑, ↗, →, ↘, ↓, ↙
direct2xy = [[0, 0], [-1, 0], [-1, -1], [0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1]]


def cast_skill(MAP, move):
    n = len(MAP)
    cloud_temp = [[False for _ in range(n)] for _ in range(n)]  # 구름 true, false
    cloud = deepcopy(cloud_temp)
    # 처음. 비바라기 시전 후 구름 위치 표시 ((N, 1), (N, 2), (N-1, 1), (N-1, 2))
    cloud[n - 1][0] = True
    cloud[n - 1][1] = True
    cloud[n - 2][0] = True
    cloud[n - 2][1] = True
    for d, s in move:
        new_cloud = deepcopy(cloud_temp)
        dx, dy = direct2xy[d]
        for y in range(n):
            for x in range(n):
                if cloud[y][x]:
                    # 1름이 d 방향에서 s만큼 이동 - 경계를 넘은 0에서 왼쪽이나 위쪽이면 -> N-1
                    new_y = (n + y + dy * s) % n
                    new_x = (n + x + dx * s) % n
                    new_cloud[new_y][new_x] = True
                    # 2. 비를 내려 칸 +1
                    MAP[new_y][new_x] += 1
        # 3. 각 구름은 대각선에 물이 1 이상인 칸의 수만큼 물 증가, 이 때 경계를 넘지 못함
        for y in range(n):
            for x in range(n):
                if new_cloud[y][x]:
                    for dx, dy in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
                        if 0 <= y + dy < n and 0 <= x + dx < n and MAP[y + dy][x + dx]:
                            MAP[y][x] += 1
        # 5. 구름 사라짐 & 바구니에 저장된 물의 양이 2 이상인 모든 칸에 구름이 생기고, 물의 양이 2 줄어든다.
        for y in range(n):
            for x in range(n):
                if new_cloud[y][x]:
                    new_cloud[y][x] = False
                elif MAP[y][x] >= 2:
                    new_cloud[y][x] = True
                    MAP[y][x] = MAP[y][x] - 2
        cloud = new_cloud
    return


def main():
    N, M = list(map(int, input().split()))
    MAP = [list(map(int, input().split())) for _ in range(N)]
    move = [list(map(int, input().split())) for _ in range(M)]
    cast_skill(MAP, move)
    print(sum([sum(ele) for ele in MAP]))


# main()

import unittest


class test_cast_skill(unittest.TestCase):
    def test_cases(self):
        move_ = [[1, 3], [3, 4], [8, 1], [4, 8]]
        MAP_ = [[0, 0, 1, 0, 2], [2, 3, 2, 1, 0], [4, 3, 2, 9, 0], [1, 0, 2, 9, 0], [8, 8, 2, 1, 0]]
        # [[0, 0, 1, 0, 0], [0, 1, 0, 1, 0], [2, 1, 0, 7, 0], [1, 0, 7, 12, 0], [6, 6, 4, 3, 0]],
        # [[2, 1, 1, 0, 0], [0, 1, 0, 1, 2], [5, 4, 5, 5, 0], [4, 5, 12, 15, 0], [4, 4, 2, 1, 0]],
        # [[4, 2, 4, 0, 2], [0, 1, 0, 1, 0], [3, 2, 3, 3, 0], [2, 3, 17, 13, 0], [2, 2, 0, 1, 0]],
        # [[2, 4, 2, 2, 4], [3, 1, 0, 5, 3], [1, 0, 1, 1, 0], [0, 1, 22, 11, 0], [4, 5, 0, 3, 2]],
        cast_skill(MAP_, move_)
        self.assertEqual(sum([sum(ele) for ele in MAP_]), 77)


unittest.main()