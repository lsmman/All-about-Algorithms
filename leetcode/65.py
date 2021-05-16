"""
날짜 : 2021-05-16
문제 : 65. Valid Number
링크 : https://leetcode.com/problems/valid-number/
"""


"""
    A valid number can be split up into these components (in order):

        1. A decimal number or an integer.
        2. (Optional) An 'e' or 'E', followed by an integer.

    A decimal number can be split up into these components (in order):

        1. (Optional) A sign character (either '+' or '-').
        2. One of the following formats:
            1. At least one digit, followed by a dot '.'.
            2. At least one digit, followed by a dot '.', followed by at least one digit.
            3. A dot '.', followed by at least one digit.
    
    An integer can be split up into these components (in order):

        1. (Optional) A sign character (either '+' or '-').
        2. At least one digit.
    
    For example, all the following are valid numbers:
        ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"],
        while the following are not valid numbers: ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"].

    Given a string s, return true if s is a valid number.
"""


class Solution:
    def __isDecimal(self, s: str) -> bool:
        if s[0] in "+-":
            s = s[1:]
        dot_index = s.find(".")
        if dot_index == -1:
            return False

        pre, post = s[:dot_index], s[dot_index + 1 :]
        # .digit pattern
        if dot_index == 0:
            return post.isdigit()
        # digit. pattern
        elif dot_index == len(s) - 1:
            return pre.isdigit()
        # digit.digit pattern
        else:
            return pre.isdigit() and post.isdigit()

    def __isInteger(self, s: str) -> bool:
        if s[0] in "+-":
            s = s[1:]
        return s.isdigit()

    def isNumber(self, s: str) -> bool:
        e_index = s.find("e")
        if e_index == -1:
            e_index = s.find("E")

        # not exist e in s
        if e_index == -1:
            # return whether s is a decimal number or an integer
            return self.__isDecimal(s) or self.__isInteger(s)

        # exist e in s
        else:
            pre = s[:e_index]  # pre-e
            post = s[e_index + 1 :]  # post-e
            # available pattern : Decimal e Interger, Integer e Interger
            return (
                pre
                and post
                and (self.__isDecimal(pre) or self.__isInteger(pre))
                and self.__isInteger(post)
            )


"""
# test code
import unittest


class TestCases(unittest.TestCase):
    def test_valid(self):
        solution = Solution()
        valid_nums = [
            "2",
            "0089",
            "-0.1",
            "+3.14",
            "4.",
            "-.9",
            "2e10",
            "-90E3",
            "3e+7",
            "+6e-1",
            "53.5e93",
            "-123.456e789",
        ]
        for vn in valid_nums:
            self.assertTrue(solution.isNumber(vn))  # True

    def test_no_valid(self):
        solution = Solution()
        no_valid_nums = ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"]
        for nvn in no_valid_nums:
            print(nvn, solution.isNumber(nvn))
            self.assertFalse(solution.isNumber(nvn))  # False

    def test_struggling(self):
        solution = Solution()
        struggle_nums_true = ["+.8"]
        struggle_nums_false = ["e2", "2e", "4e+", "+.", "4.."]
        for sn in struggle_nums_true:
            self.assertTrue(solution.isNumber(sn))
        for sn in struggle_nums_false:
            self.assertFalse(solution.isNumber(sn))


unittest.main()
"""