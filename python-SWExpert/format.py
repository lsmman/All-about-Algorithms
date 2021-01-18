"""
시간 : 50개 테스트케이스를 합쳐서 C의 경우 3초 / C++의 경우 3초 / Java의 경우 3초 / python의 경우 15초
메모리 : 힙, 정적 메모리 합쳐서 256MB 이내, 스택 메모리 1MB 이내

"""

import sys


def solution(N):
    return 0


def main():
    sys.stdin = open("python-SWExpert\\input.txt", "r")

    T = int(input())
    for t in range(1, T + 1):
        N = int(input())
        # 여러 개 : list(map(int, input().split()))
        # 여러 개 리스트 [list(map(int, input().split())) for _ in range(N)]
        ans = solution(N)
        print("#{} {}".format(t, ans))


if __name__ == "__main__":
    main()
