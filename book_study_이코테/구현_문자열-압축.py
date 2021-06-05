# -*- coding: utf-8 -*-

import unittest

"""
압축할 문자열 s가 매개변수로 주어질 때, 
1개 이상 단위로 문자열을 잘라 압축하여 표현한 문자열 중 가장 짧은 것의 길이를 return 하도록 solution 함수를 완성.

input
  s -> str
output
  압축한 문자열 중 가장 짧은 것의 길이
limit
  1 <= s <= 1000, s는 알파벳 소문자
  time : 1 second
  memory : 128 MB
analysis
  시간복잡도 : $O(N^2)$
  공간복잡도 : $O(N)$
본 링크
  https://programmers.co.kr/learn/courses/30/lessons/60057?language=python3
"""


def solve(s):
    leng = len(s)
    min_leng = 10000
    # 문자를 잘라 압축하는 단위 unit (1 to half of length)
    for unit in range(1, leng // 2 + 2):
        # unit 단위로 문자열을 잘라 압축된 길이를 구한다.
        # abcdefgh이면 ab, cd, ef, gh로 잘라 비교하여 길이를 구한다.
        pre = s[:unit]
        unit_cnt = [1]  # 압축된 count를 저장하는 배열, 나중에 길이 계산을 거치게 된다.
        unit_leng = leng % unit  # unit으로 나누어 떨어지지 않는 경우 마지막 단위는 압축이 되지 않으므로 여분 길이을 더해준다.

        # unit씩 비교하여 같으면 cnt를 올려주고 다르면 새로운 cnt를 등록해준다.
        for i in range(unit, leng // unit * unit, unit):
            cur = s[i : i + unit]
            if pre == cur:
                unit_cnt[-1] += 1
            else:
                unit_cnt.append(1)
                pre = cur

        # unit cnt 정보를 이용하여 전체 길이 unit_leng를 구한다.
        for u in unit_cnt:
            if u > 1:
                # 2이상 반복되는 경우 숫자만큼 leng를 더해준다. str의 len을 구하는 연산을 통해 10이상 반복 되었을 때 맞게 적용되도록 한다.
                unit_leng += len(str(u))
            unit_leng += unit

        min_leng = min(unit_leng, min_leng)
    return min_leng


class testSolve(unittest.TestCase):
    def testcase1(self):
        self.assertEqual(solve("aabbaccc"), 7)

    def testcase2(self):
        self.assertEqual(solve("ababcdcdababcdcd"), 9)

    def testcase3(self):
        self.assertEqual(solve("abcabcdede"), 8)

    def testcase4(self):
        self.assertEqual(solve("abcabcabcabcdededededede"), 14)

    def testcase5(self):
        self.assertEqual(solve("xababcdcdababcdcd"), 17)

    def testcase6(self):
        self.assertEqual(solve("abcabcdede"), 8)

    def testcase7(self):
        self.assertEqual(solve("ababcdcdababcdcd"), 9)


unittest.main()