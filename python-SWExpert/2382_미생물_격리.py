"""
[제약사항]

1. 시간제한 : 최대 50개 테스트 케이스를 모두 통과하는데, C/C++/Java 모두 5초
2. 정사각형 한 변의 셀 N (5 ≤ N ≤ 100)
3. 초기 미생물 군집의 개수 K는 5이상 1,000이하의 정수이다. (5 ≤ K ≤ 1,000)
4. 격리 시간 M은 1이상 1,000이하의 정수이다. (1 ≤ M ≤ 1,000)
5. 최초 약품이 칠해진 가장자리 부분 셀에는 미생물 군집이 배치되어 있지 않다.
6. 최초에 둘 이상의 군집이 동일한 셀에 배치되는 경우는 없다.
7. 각 군집 내 미생물 수는 1 이상 10,000 이하의 정수이다.
8. 군집의 이동방향은 상하좌우 4방향 중 한 방향을 가진다. (상: 1, 하: 2, 좌: 3, 우: 4)
9. 주어진 입력으로 진행하였을 때, 동일한 셀에 같은 미생물 수를 갖는 두 군집이 모이는 경우는 발생하지 않는다.
10.  각 군집의 정보는 세로 위치, 가로 위치, 미생물 수, 이동 방향 순으로 주어진다. 각 위치는 0번부터 시작한다.
"""

import sys
from collections import defaultdict


def get_idx_of_max_amount(microbes, v):
    amount = 2
    max_amount, max_idx = -1, -1
    for ele in v:
        if max_amount < microbes[ele][amount]:
            max_idx = ele
            max_amount = microbes[ele][amount]
    return max_idx


def solution(N, M, K, microbes):
    # microbes.__form__ = (y, x, amount, direct)
    # (up: 1, down: 2, left: 3, right: 4)
    direct = [(0, 0), (0, -1), (0, 1), (-1, 0), (1, 0)]  # x, y
    opp_side = [0, 2, 1, 4, 3]
    boundry = [0, N - 1]
    y, x, amount, di = range(4)

    for __ in range(M):
        visit = defaultdict(list)
        for m_idx in range(len(microbes) - 1, -1, -1):
            mb = microbes[m_idx]
            dx, dy = direct[mb[di]]
            mb[y] += dy
            mb[x] += dx

            if mb[y] in boundry or mb[x] in boundry:
                mb[di] = opp_side[mb[di]]
                mb[amount] = mb[amount] // 2
                if not mb[amount]:
                    microbes.pop(m_idx)
            else:
                visit[(mb[x], mb[y])].append(m_idx)

        m_indexes = set(range(len(microbes)))
        for v in visit.values():
            if len(v) >= 2:
                max_idx = get_idx_of_max_amount(microbes, v)
                microbes[max_idx][amount] = sum([microbes[ele][amount] for ele in v])
                m_indexes -= set(v) - set([max_idx])
        microbes = [microbes[i] for i in m_indexes]
    return sum([mb[amount] for mb in microbes])


def main():
    sys.stdin = open("python-SWExpert\\input.txt", "r")

    T = int(input())
    for t in range(1, T + 1):
        N, M, K = list(map(int, input().split()))
        microbes = [list(map(int, input().split())) for _ in range(K)]
        ans = solution(N, M, K, microbes)
        print("#{} {}".format(t, ans))


if __name__ == "__main__":
    main()

# 1 145
# 2 5507
# 3 9709
# 4 2669
# 5 3684
# 6 774
# 7 4797
# 8 8786
# 9 1374
# 10 5040
