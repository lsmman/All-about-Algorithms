"""
시간 : 50개 테스트케이스를 합쳐서 C의 경우 5초 / C++의 경우 5초 / Java의 경우 5초 / python의 경우 25초
메모리 : 힙, 정적 메모리 합쳐서 256MB 이내, 스택 메모리 1MB 이내

"""

import sys
from itertools import combinations

from time import time

s = time()

sys.stdin = open("python-SWExpert\\input.txt", "r")

t = int(input())

for test_case in range(t):
    d, w, k = map(int, input().split())
    raw = [list(map(int, input().split())) for _ in range(d)]

    def check():
        global d, w, k
        for col in range(w):
            flag = 0
            cnt = 1
            for row in range(d - 1):
                if d - row < k and cnt == 1:
                    break
                if data[row][col] == data[row + 1][col]:
                    cnt += 1
                else:
                    cnt = 1
                if cnt == k:
                    flag = 1
                    break
            if not flag:
                return False
        return True

    def solve(depth):
        global d, w, res, data

        if depth == d:
            res = min(res, d)
            return
        comb = combinations(idx, depth)
        for c in comb:
            for j in range(2):
                for i in c:
                    data[i] = drug[j]
                if check():
                    res = min(res, depth)
                    return
                data = raw[:]

    data = raw[:]
    drug = [[0] * w, [1] * w]
    idx = list(range(d))
    res = float("inf")
    if check() or k <= 1:
        res = 0
    else:
        for i in range(1, d + 1):
            if i >= res:
                break
            solve(i)

    print("#{} {}".format(test_case + 1, res))

print(time() - s)
# 1 2
# 2 0
# 3 4
# 4 2
# 5 2
# 6 0
# 7 3
# 8 2
# 9 3
# 10 4
