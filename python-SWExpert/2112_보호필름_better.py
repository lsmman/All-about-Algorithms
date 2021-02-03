"""
시간 : 50개 테스트케이스를 합쳐서 C의 경우 5초 / C++의 경우 5초 / Java의 경우 5초 / python의 경우 25초
메모리 : 힙, 정적 메모리 합쳐서 256MB 이내, 스택 메모리 1MB 이내

"""

import sys
from itertools import combinations, product

# A 0 False
# B 1 True
def solution(D, W, K, flim):
    for k in range(K):
        for pattern in product((0, 1), repeat=k):
            for comb in combinations(range(D), k):
                for line in zip(*flim):
                    line = list(line)
                    for i in range(k):
                        line[comb[i]] = bool(pattern[i])
                    preq = count = 0
                    for cur in line:
                        if preq ^ cur:  # 다르면
                            count = 1
                            preq = cur
                        else:  # 같으면
                            count += 1
                            if count >= K:  # 조건 충족, break
                                break
                    else:  # 조건 미 충족 break, 다른 경우의 수 확인
                        break
                else:  # 모든 조건 충족. 결과 출력
                    return k
    return K


def main():
    sys.stdin = open("python-SWExpert\\input.txt", "r")

    T = int(input())
    for t in range(1, T + 1):
        D, W, K = map(int, input().split())
        flim = [list(map(int, input().split())) for _ in range(D)]
        ans = solution(D, W, K, flim)
        print("#{} {}".format(t, ans))

from time import time
if __name__ == "__main__":
    s = time()
    main()
    print(time()-s)
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
