"""
시간 : 50개 테스트케이스를 합쳐서 C의 경우 3초 / C++의 경우 3초 / Java의 경우 3초 / python의 경우 15초
메모리 : 힙, 정적 메모리 합쳐서 256MB 이내, 스택 메모리 1MB 이내

"""

import sys
from collections import defaultdict


def solution(N, atomics):
    # x, y, di, K
    # direct = 0-상, 1-하, 2-좌, 3-우
    direct = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    limit = 4002
    energy = 0
    x, y, di, K = (0, 1, 2, 3)
    for a in atomics:
        a[x] = (a[x] + 1000) * 2
        a[y] = (a[y] + 1000) * 2
    while atomics:
        visit = defaultdict(set)
        delete = set()
        for i, atomic in enumerate(atomics):
            dx, dy = direct[atomic[di]]
            new_x = atomic[x] + dx
            new_y = atomic[y] + dy
            if new_x < 0 or new_x > limit or new_y < 0 or new_y > limit:
                atomic[K] = 0
                delete.add(i)
            else:
                visit[(new_x, new_y)].add(i)
                atomic[x], atomic[y] = new_x, new_y
        for v in visit.values():
            if len(v) > 1:
                delete.update(v)

        if delete:
            new_atomics = []
            for i, atomic in enumerate(atomics):
                if i in delete:
                    energy += atomic[K]
                else:
                    new_atomics.append(atomic)
            atomics = new_atomics
    return energy


def main():
    sys.stdin = open("python-SWExpert\\input.txt", "r")

    T = int(input())
    for t in range(1, T + 1):
        N = int(input())
        atomics = [list(map(int, input().split())) for _ in range(N)]
        ans = solution(N, atomics)
        print("#{} {}".format(t, ans))


if __name__ == "__main__":
    # main()
    solution(-1, [[-2, 0, 3, 3], [-1, 0, 3, 2], [0, 0, 2, 5], [1, 0, 2, 4], [0, -1, 0, 6]])

# 1 24
# 2 0
# 3 7
# 4 10
# 5 16
# 6 17
