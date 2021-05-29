################### 설명 적어야함
import unittest

"""
게임 캐릭터가 맵 안에서 움직이는 시스템을 개발
input
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
    get_left_di = lambda di: (di + 3) % 4
    get_back_di = lambda di: (di + 2) % 4
    get_next_xy = lambda loc, di: [loc[0] + direction[di][0], loc[1] + direction[di][1]]
    check_loc_is_valid = lambda x, y: (0 <= x < M) and (0 <= y < N) and MAP[y][x] == land

    visited[myloc[1]][myloc[0]] = True
    while True:
        next_x, next_y = get_next_xy(myloc, get_left_di(mydi))
        if check_loc_is_valid(next_x, next_y) and not visited[next_y][next_x]:
            visited[next_y][next_x] = True
            cnt += 1
            myloc = [next_x, next_y]
            mydi = get_left_di(mydi)
            continue

        for di_idx in range(4):
            next_x, next_y = get_next_xy(myloc, di_idx)
            if check_loc_is_valid(next_x, next_y) and not visited[next_y][next_x]:
                break
        # 네 방향이 모두 가본 칸이거나 바다로 되어 있는 칸인 경우
        else:
            myloc = get_next_xy(myloc, get_back_di(mydi))  # 뒤로 한 칸
            if not check_loc_is_valid(myloc[1], myloc[0]):
                return cnt
        mydi = get_left_di(mydi)
    return 0


class testSolve(unittest.TestCase):
    def testcase(self):
        N, M = 4, 4
        myloc = [1, 1]
        mydi = 0
        MAP = [[1, 1, 1, 1], [1, 0, 0, 1], [1, 1, 0, 1], [1, 1, 1, 1]]
        self.assertEqual(solve(N, M, myloc, mydi, MAP), 3)


unittest.main()