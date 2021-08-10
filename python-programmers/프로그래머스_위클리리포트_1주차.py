"""
위클리 리포트 1주차
https://programmers.co.kr/learn/courses/30/lessons/82612?language=python3

시간 복잡도 : O(n^2)
공간 복잡도 : O(n)
"""

def solution(price, money, count):
    return max(price * count * (count+1) // 2 - money, 0)

import unittest

class test(unittest.TestCase):
    def test_case(self):
        self.assertEqual(solution(3, 20 ,4), 10)


unittest.main()
