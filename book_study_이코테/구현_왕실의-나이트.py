import unittest

"""
왕실 정원은 체스판과 같은 8 x 8 좌표 평면이다. 
나이트가 특정한 한 칸에 서 있을 때 나이트가 이동할 수 있는 경우의 수를 구하라
나이트는 L자 형태로만 이동할 수 있으며, 정원(map) 밖으로 벗어날 수 없다.
  1. 수평 두 칸 이동 후 수직 한 칸 이동
  2. 수직 두 칸 이동 후 수평 한 칸 이동

input
  loc -> str : 나이트가 현재 위치한 곳의 좌표, 두 문자로 구성 ex) a1
output
  cnt -> int : 나이트가 이동할 수 있는 경우의 수
limit
  time : 1 second
  memory : 128 MB
analysis
  시간복잡도 : O(1)
  공간복잡도 : O(1)
"""


def solve(loc):
    # 나이트가 맵 안에서 L자로 이동할 수 있는 좌표의 수 구하기
    cnt = 0
    limit = 8
    x, y = ord(loc[0]) - ord("a"), int(loc[1]) - 1
    steps = [[-1, 2], [2, -1], [-1, -2], [-2, -1], [1, 2], [2, 1], [1, -2], [-2, 1]]

    # 이동 가능한 8방위의 좌표로 이동했을 때 맵을 벗어나지 않는다면 cnt += 1
    for dx, dy in steps:
        if (0 <= x + dx < limit) and (0 <= y + dy < limit):
            cnt += 1
    return cnt


class testSolve(unittest.TestCase):
    def testcase(self):
        self.assertEqual(solve("a1"), 2)


unittest.main()