import sys


def solution(arr):
    for i in range(9):
        if not len(set(arr[i])) == 9:
            return 0

        if not len(set([a[i] for a in arr])) == 9:
            return 0

    points = [(0, 0), (0, 3), (0, 6), (3, 0), (3, 3), (3, 6), (6, 0), (6, 3), (6, 6)]
    for x, y in points:
        if not len(set(arr[x][y : y + 3] + arr[x + 1][y : y + 3] + arr[x + 2][y : y + 3])) == 9:
            return 0
    return 1


def main():
    sys.stdin = open("python-programmers/input.txt")

    T = int(input())
    for test_case in range(1, T + 1):
        arr = []
        for _ in range(9):
            arr.append(list(map(int, input().split())))
        ans = solution(arr)
        print("#{} {}".format(test_case, ans))


if __name__ == "__main__":
    main()
