"""
시간 : 50개 테스트케이스를 합쳐서 C의 경우 3초 / C++의 경우 3초 / Java의 경우 3초 / python의 경우 15초
메모리 : 힙, 정적 메모리 합쳐서 256MB 이내, 스택 메모리 1MB 이내

"""

import sys


def solution(M, A, user, AP):
    return 0


def main():
    sys.stdin = open("python-SWExpert\\input.txt", "r")

    T = int(input())
    for t in range(1, T + 1):
        M, A = list(map(int, input().split()))
        user = [list(map(int, input().split())) for _ in range(2)]
        AP = [list(map(int, input().split())) for _ in range(A)]
        ans = solution(M, A, user, AP)
        print("#{} {}".format(t, ans))


if __name__ == "__main__":
    main()
# 1 1200
# 2 3290
# 3 16620
# 4 40650
# 5 52710
