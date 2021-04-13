import unittest


class test_method(unittest.TestCase):
    def test_solution(self):
        result1 = solution([[1, 0, 0, 3], [2, 0, 0, 0], [0, 0, 0, 2], [3, 0, 1, 0]], 1, 0)
        self.assertEqual(result1, 14)

        result2 = solution([[3, 0, 0, 2], [0, 0, 1, 0], [0, 1, 0, 0], [2, 0, 0, 3]], 0, 1)
        self.assertEqual(result2, 16)

    def test_get_total_count(self):
        result = get_total_count(
            [[1, 0, 0, 3], [2, 0, 0, 0], [0, 0, 0, 2], [3, 0, 1, 0]][
                -1, -1, (0, 0), (3, 2), (1, 0), (2, 3), (0, 3), (3, 0), -1, -1, -1, -1, -1
            ](1, 0)(1, 2, 3)(0, 0, 0)
        )
        self.assertEqual(result, 0)

    def 
from itertools import permutations, product


def get_distance(board, from_, to):

    return 0


def get_total_count(board, cards, srt, order, p):
    cnt = 0
    cur = srt
    enter = 1
    for point, plus in zip(order, p):
        cnt += get_distance(board, cur, cards[point + plus]) + enter
        cnt += get_distance(board, cards[point + plus], cards[point + 1 - plus]) + enter
        cur = cards[point + 1 - plus]
    return cnt


def solution(board, r, c):
    answer = 10000001
    n = 4
    max_card_num = 12
    card_range = 0
    cards = [-1 for _ in range(max_card_num + 1)]
    srt = (r, c)

    # 카드 정보 arr 만들기
    for i in range(n):
        for j in range(n):
            card = board[i][j]
            if card:
                card_range = max(card, card_range)
                if cards[2 * card] == -1:
                    cards[2 * card] = (i, j)
                else:
                    cards[2 * card + 1] = (i, j)
    for order in permutations(range(1, card_range + 1), card_range):
        for p in product([0, 1], repeat=card_range):
            count = get_total_count(board, cards, srt, order, p)
            answer = min(count, answer)
    return answer


if __name__ == "__main__":
    # unittest.main()
    print(solution([[1, 0, 0, 3], [2, 0, 0, 0], [0, 0, 0, 2], [3, 0, 1, 0]], 1, 0))
