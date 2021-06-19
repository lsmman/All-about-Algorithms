# -*- coding: utf-8 -*-

import unittest

"""
특정조건에서 사용할 수 있는 필살기인 럭키 스트레이트 기술이 있습니다.
그 특정 조건은 현재 캐릭터의 점수를 N이라고 할 때 자릿수를 기준으로 점수 N을 반으로 나누어 왼쪽 부분의 각 자릿수의 합과 오른쪽 부분의 각 자릿수의 합을 더한 값이 동일한 상황을 의미합니다.
N의 자릿수는 짝수로 주어집니다.
예를 들어 점수가 123402라면 왼쪽 부분의 각 자릿수 합은 1+2+3, 오른쪽 부분의 각 자릿수 합은 4+0+2이므로 두 합이 6으로 동일해 럭키 스트레이트를 사용할 수 있습니다.

input
  N -> int : 현재 점수
output
  럭키 스트레이트를 사용할 수 있으면 "LUCKY"
  사용할 수 없다면 "READY"
limit
  time : 1 second
  memory : 256 MB
analysis
  시간복잡도 : O(N)
  공간복잡도 : O(N)
"""


def solve(N):
    str_N = str(N)
    mid = len(str_N) // 2
    pre, post = 0, 0
    for i in range(mid):
        pre += int(str_N[i])
        post += int(str_N[mid + i])

    if pre == post:
        return "LUCKY"
    else:
        return "READY"


class testSolve(unittest.TestCase):
    def testcase1(self):
        self.assertEqual(solve(123402), "LUCKY")

    def testcase2(self):
        self.assertEqual(solve(7755), "READY")


unittest.main()