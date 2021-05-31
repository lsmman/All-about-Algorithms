################### 설명 적어야함
import unittest

"""
게임 캐릭터가 맵 안에서 움직이는 시스템을 개발
- 맵은 N x M 크기의 직사각형으로 각각 칸이 육지 또는 바다
- 캐릭터는 상하좌우로 움직일 수 있고, 바다로 되어 있는 공간에는 갈 수 없다.

캐릭터 움직임 매뉴얼
1. 현재 위치에서 현재 방향을 기준으로 왼쪽 방향 (반시계 90도)부터 차례대로 갈 곳을 정한다.
2. 캐릭터의 바로 왼쪽방향에 가보지 않은 칸이 존재한다면 왼쪽 방향으로 회전한다음 왼쪽으로 한 칸 전진
   왼쪽 방향 칸이 가보았던 칸이면 왼쪽 방향으로 회전만 수행
3. 네 방향 모두 이미 가본 칸이거나 바다로 되어 있는 칸인 경우, 바라보는 방향을 유지한 채로 한 칸 뒤로 가고 1단계로 돌아간다.
   단, 이 때 뒤쪽 방향이 바다인 칸이라 뒤로 갈 수 없는 경우에는 움직임을 멈춘다.

input
  N -> int : row limit
  M -> int : col limit
  myloc -> list : 현재 위치 [x, y]
  MAP -> 2d list : N x M MAP, 각 칸에 land(0)과 sea(1) 정보가 포함
output
  count -> int : visit한 valid한 타일의 개수
limit
  N >= 3 
  M <= 50
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
        # 왼쪽 방향으로 전진한 칸이 valid하고 가보지 않은 칸이면 왼쪽으로 회전하고 한 칸을 전진
        if check_loc_is_valid(next_x, next_y) and not visited[next_y][next_x]:
            visited[next_y][next_x] = True
            cnt += 1  # cnt += 1 when visit valid and not-visited loc
            myloc = [next_x, next_y]
            mydi = get_left_di(mydi)

        # 그 외 경우 방향만 left 90 degree로
        else:
            mydi = get_left_di(mydi)

        # 네 방향 중 가볼 수 있는 loc가 있으면 break
        for di_idx in range(4):
            next_x, next_y = get_next_xy(myloc, di_idx)

            if check_loc_is_valid(next_x, next_y) and not visited[next_y][next_x]:
                break
        # 네 방향이 모두 가본 칸이거나 갈 수 없는 타일인 경우
        else:
            myloc = get_next_xy(myloc, get_back_di(mydi))  # 뒤로 한 칸, 방향은 유지
            if not check_loc_is_valid(myloc[1], myloc[0]):  # 뒤로 간 칸이 갈 수 없는 타일이면
                return cnt
    return 0


class testSolve(unittest.TestCase):
    def testcase(self):
        N, M = 4, 4
        myloc = [1, 1]
        mydi = 0
        MAP = [[1, 1, 1, 1], [1, 0, 0, 1], [1, 1, 0, 1], [1, 1, 1, 1]]
        self.assertEqual(solve(N, M, myloc, mydi, MAP), 3)


unittest.main()