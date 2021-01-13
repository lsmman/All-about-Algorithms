"""
시간 : 50개 테스트케이스를 합쳐서 C의 경우 3초 / C++의 경우 3초 / Java의 경우 3초
메모리 : 힙, 정적 메모리 합쳐서 256MB 이내, 스택 메모리 1MB 이내

"""

import sys
import heapq


def solution(N, K, nums):
    kth_max = preq = k = 0
    word_len = N // 4
    nums = nums + nums[:word_len]
    heap = list()
    for i in range(N):
        heapq.heappush(heap, (-int(nums[i : i + word_len], 16)))

    preq = 1
    while k < K:
        kth_max = heapq.heappop(heap)
        if not preq == kth_max:
            k += 1
        preq = kth_max
    return -kth_max


def main():
    sys.stdin = open("python-SWExpert\input.txt", "r")

    T = int(input())
    for t in range(1, T + 1):
        N, K = map(int, input().split())
        nums = input()
        ans = solution(N, K, nums)
        print("#{} {}".format(t, ans))


if __name__ == "__main__":
    main()

# 1 503
# 2 55541
# 3 334454
# 4 5667473
# 5 182189737
