import unittest

"""
00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 구하라
### input
N : N시
### output
00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수
"""


def solve(N):
    # 완전탐색
    cnt = 0
    for h in range(N + 1):
        for m in range(60):
            for s in range(60):
                if "3" in str(h) + str(m) + str(s):
                    cnt += 1
    return cnt


def solve_efficient(N):
    cnt = 0
    cnt_include_3 = 3600
    cnt_not_include_3 = 1575

    for n in range(N + 1):
        if "3" in str(n):
            cnt += cnt_include_3
        else:
            cnt += cnt_not_include_3
    return cnt


class testSolve(unittest.TestCase):
    def testcase(self):
        self.assertEqual(solve(5), 11475)


unittest.main()