import sys
from collections import defaultdict


def solution(arr, n):
    maxs = [0] * n
    view = [0] * n
    for i in range(n - 1):
        maxs[i] = max(arr[i], arr[i + 1])
    for i in range(2, n - 2):
        view[i] = max(0, arr[i] - max(maxs[i - 2], maxs[i + 1]))
    return sum(view)


def main():
    # sys.stdin = open("python-programmers/1206.txt")

    T = 10
    for test_case in range(1, T + 1):
        length = int(input())
        arr = list(map(int, input().split()))
        ans = solution(arr, length)
        print("#{} {}".format(test_case, ans))


if __name__ == "__main__":
    main()
