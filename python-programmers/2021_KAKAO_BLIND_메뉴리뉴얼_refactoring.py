"""
1번 신규아이디 14:11.11
구현, 문자열

2번 메뉴리뉴얼 15:31.65
순열, count 문제

3번 순위검색 - 정확, 효율 00:58:17.82
문자열, binsearch
못품

4번 합승택시 요금 00:44:37.52
graph short path
"""


from collections import defaultdict
from itertools import combinations


def solution(orders, course):
    answer = []
    for c_num in course:
        menu_cnt = defaultdict(int)
        for o in orders:
            if len(o) < c_num:
                continue
            for c in combinations(o, c_num):
                menu_cnt[tuple(sorted(c))] += 1

        max_cnt = max(menu_cnt.values()) if menu_cnt else -1
        if max_cnt < 2:
            continue
        for k, v in menu_cnt.items():
            if v == max_cnt:
                answer.append("".join(k))

    return sorted(answer)