import unittest

"""
plan에 따라 L, R, U, D로 방향으로 이동 후 최종 좌표 return
input
  N -> int : N x N 공간의 크기 N
  plan -> list : 이동 계획
output
  [x, y] : 최종 좌표
limit
  1 <= N <= 100
  1 <= len(plan) <= 100
  time : 1 second
  memory : 128 MB
analysis
  시간복잡도 : O(N)
  공간복잡도 : O(1)
"""


def solve(N, plan):
    # plan에 따라 L, R, U, D로 방향으로 이동 후 최종 좌표 return
    plan2xy = {"L": [0, -1], "R": [0, 1], "U": [-1, 0], "D": [1, 0]}
    x, y = 1, 1
    for p in plan:
        dx, dy = plan2xy[p]
        if 1 <= x + dx <= N:
            x += dx
        if 1 <= y + dy <= N:
            y += dy

    return [x, y]


class testSolve(unittest.TestCase):
    def testcase(self):
        self.assertEqual(solve(5, ["R", "R", "R", "U", "D", "D"]), [3, 4])


unittest.main()