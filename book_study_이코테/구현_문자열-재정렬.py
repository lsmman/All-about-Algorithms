# -*- coding: utf-8 -*-

import unittest

"""
알파벳 대문자와 숫자(0~9)로만 구성된 문자열이 입력으로 주어집니다. 
이때 모든 알파벳을 오름차순으로 정렬하여 이어서 출력한 뒤에, 그 뒤에 모든 숫자를 더한 값을 이어서 출력합니다.
예를 들어 K1KA5CB7이라는 값이 들어오면 ABCKK13을 출력합니다.

input
  S -> str
output
  문자열 - 알파벳은 오름차순, 숫자는 더한 값을 이어서 출력
limit
  time : 1 second
  memory : 128 MB
analysis
  시간복잡도 : O(N^2)
  공간복잡도 : O(N)
"""

from bisect import insort


def solve(S):
    result = []
    sum_num = 0
    for s in S:
        if s.isdigit():
            sum_num += int(s)
        else:
            insort(result, s)
    return "".join(result) + str(sum_num)


class testSolve(unittest.TestCase):
    def testcase1(self):
        self.assertEqual(solve("K1KA5CB7"), "ABCKK13")

    def testcase2(self):
        self.assertEqual(solve("AJKDLSI412K4JSJ9D"), "ADDIJJJKKLSS20")


unittest.main()