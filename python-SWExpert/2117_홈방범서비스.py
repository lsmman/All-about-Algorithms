"""
시간 : 50개 테스트케이스를 합쳐서 C의 경우 3초 / C++의 경우 3초 / Java의 경우 3초 / python의 경우 15초
메모리 : 힙, 정적 메모리 합쳐서 256MB 이내, 스택 메모리 1MB 이내

"""

import sys


def solution(N, M, MAP):
    # return : 손해를 보지 않으면서 홈방범 서비스를 가장 많은 집들에 제공하는 서비스 영역을 찾았을 때, 서비스를 받는 집들의 수이다.
    max_home = 0
    K_limit = (N // 2) * 2 + 2
    costs = [k * k + (k - 1) * (k - 1) for k in range(K_limit)]
    homes = []
    for y in range(N):
        for x in range(N):
            if MAP[x][y]:
                homes.append((x, y))

    for y in range(N):
        for x in range(N):
            count_of_home_in_area = [0 for _ in range(2 * N)]
            sum_val = 0
            for hx, hy in homes:
                count_of_home_in_area[abs(hx - x) + abs(hy - y) + 1] += 1
            for i in range(K_limit):
                sum_val += count_of_home_in_area[i]
                if sum_val * M >= costs[i]:
                    max_home = max(max_home, sum_val)
    return max_home


def main():
    sys.stdin = open("python-SWExpert\\input.txt", "r")

    T = int(input())
    for t in range(1, T + 1):
        N, M = list(map(int, input().split()))
        MAP = [list(map(int, input().split())) for _ in range(N)]
        ans = solution(N, M, MAP)
        print("#{} {}".format(t, ans))


if __name__ == "__main__":
    main()
# 1 5
# 2 4
# 3 24
# 4 48
# 5 3
# 6 65
# 7 22
# 8 22
# 9 78
# 10 400
