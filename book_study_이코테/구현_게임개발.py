################### 설명 적어야함
import unittest

"""
게임 캐릭터가 맵 안에서 움직이는 시스템을 개발
input
  N -> int : row limit
  M -> int : col limit
  myloc -> list : 현재 위치 [x, y]
  MAP -> 2d list : N x M MAP, 각 칸에 land(0)과 sea(1) 정보가 포함
output
limit
  time : 1 second
  memory : 128 MB
analysis
  시간복잡도 : O(NM)
  공간복잡도 : O(NM)
"""


def solve(N, M, myloc, mydi, MAP):
    # 게임 개발
    cnt = 1
    land = 0  # sea = 1
    direction = [[0, -1], [1, 0], [0, 1], [-1, 0]]
    visited = [[False for x in range(M)] for y in range(N)]
    get_left_di = lambda di: (di + 3) % 4  # turn left 90 degree
    get_back_di = lambda di: (di + 2) % 4  # turn 180 degree
    get_next_xy = lambda loc, di: [
        loc[0] + direction[di][0],
        loc[1] + direction[di][1],
    ]  # get next loc through direction
    check_loc_is_valid = (
        lambda x, y: (0 <= x < M) and (0 <= y < N) and MAP[y][x] == land
    )  # check loc in MAP and loc is land

    visited[myloc[1]][myloc[0]] = True
    while True:
        next_x, next_y = get_next_xy(myloc, get_left_di(mydi))  # get loc to left direction
        if check_loc_is_valid(next_x, next_y) and not visited[next_y][next_x]:
            visited[next_y][next_x] = True
            cnt += 1  # cnt += 1 when visit valid and not-visited loc
            myloc = [next_x, next_y]
            mydi = get_left_di(mydi)
            continue

        # 네 방향 검사
        for di_idx in range(4):
            next_x, next_y = get_next_xy(myloc, di_idx)
            # 네 방향 중 가볼 수 있는 loc가 있을 때 break
            if check_loc_is_valid(next_x, next_y) and not visited[next_y][next_x]:
                break
        # 네 방향이 모두 가본 칸이거나 갈 수 없는 타일인 경우
        else:
            myloc = get_next_xy(myloc, get_back_di(mydi))  # 뒤로 한 칸, 방향은 유지
            if not check_loc_is_valid(myloc[1], myloc[0]):  # 뒤로 간 칸이 갈 수 없는 타일이면
                return cnt
            continue
        mydi = get_left_di(mydi)  # 그 외 경우 방향만 left 90 degree로
    return 0


class testSolve(unittest.TestCase):
    def testcase(self):
        N, M = 4, 4
        myloc = [1, 1]
        mydi = 0
        MAP = [[1, 1, 1, 1], [1, 0, 0, 1], [1, 1, 0, 1], [1, 1, 1, 1]]
        self.assertEqual(solve(N, M, myloc, mydi, MAP), 3)


unittest.main()