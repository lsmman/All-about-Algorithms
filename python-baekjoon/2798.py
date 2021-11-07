# https://www.acmicpc.net/problem/2798

"""
### New blackjack
M 달성해야하는 수 - M을 넘으면 안됨
N 장 중 3장 뽑음
못찾는 경우는 주어지지않음
"""


import unittest


def get_equal_or_smaller(input_num, numbers):
    # list의 수 중 input number보다 작거나 같은 수를 binary search를 이용해서 찾는다.
    left = 0
    right = len(numbers)-1
    if not numbers or input_num < numbers[0]:
        return -1
    while left <= right:
        mid = (left+right) // 2
        cur = numbers[mid]
        if cur == input_num:
            left = mid+1
            break
        elif cur > input_num:
            right = mid-1
        else:
            left = mid+1
    return left-1


def appy_new_blackjack(N, target, numbers) -> int:
    # numbers timsort 정렬
    numbers.sort()
    answer = sum(numbers[-3:])
    if answer <= target:
        return answer

    answer = sum(numbers[:3])
    min_diff = target - answer
    # 첫 수 정해두고 늘리면서 탐색
    for idx_1, first in enumerate(numbers):
        limit = (target - first) // 2
        min_sum = sum(numbers[idx_1:idx_1+3])
        if target == min_sum:
            return target
        elif target < min_sum:
            continue
        for idx_2, second in enumerate(numbers[idx_1+1:]):
            if limit < second:
                break
            third = target - first - second

            idx_3 = get_equal_or_smaller(third, numbers)
            third = numbers[idx_3]
            if idx_3 == -1 or idx_2 == idx_3:
                break

            cur_answer = first + second + third
            if cur_answer == target:
                return target

            cur_diff = target - cur_answer
            if cur_diff and min_diff > cur_diff:
                answer = cur_answer
                min_diff = cur_diff

    return answer


def main():
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))
    result = appy_new_blackjack(N, M, numbers)
    print(result)


# main()


class testcase(unittest.TestCase):
    def test1_get_equal_or_smaller(self):
        input_num = 7
        numbers = [5, 6, 8, 9]
        result = get_equal_or_smaller(input_num, numbers)
        self.assertEqual(6, numbers[result])

    def test2_get_equal_or_smaller(self):
        input_num = 7
        numbers = [5, 6, 7, 8, 9]
        result = get_equal_or_smaller(input_num, numbers)
        self.assertEqual(7, numbers[result])

    def test3_get_equal_or_smaller(self):
        input_num = 7
        numbers = [8, 9]
        result = get_equal_or_smaller(input_num, numbers)
        self.assertEqual(-1, result)

    def test4_get_equal_or_smaller(self):
        input_num = 139
        numbers = [36, 93, 138, 181, 185, 214, 216, 245, 295, 315]
        result = get_equal_or_smaller(input_num, numbers)
        self.assertEqual(138, numbers[result])

    def test5_get_equal_or_smaller(self):
        input_num = 8
        numbers = [4, 5, 6, 7]
        result = get_equal_or_smaller(input_num, numbers)
        self.assertEqual(7, numbers[result])

    def test1_appy_new_blackjack(self):
        N = 5
        M = 21
        numbers = [5, 6, 7, 8, 9]
        result = appy_new_blackjack(N, M, numbers)
        self.assertEqual(21, result)

    def test2_appy_new_blackjack(self):
        N = 10
        M = 500
        numbers = [93, 181, 245, 214, 315, 36, 185, 138, 216, 295]
        result = appy_new_blackjack(N, M, numbers)
        self.assertEqual(497, result)


unittest.main()
