import sys


def solution(arr):
    maxval = -1
    n = len(arr)
    for i in range(n):
        horizon_sum = sum(arr[i])
        vert_sum = sum([line[i] for line in arr])
        maxval = max(maxval, horizon_sum)
        maxval = max(maxval, vert_sum)

    right_diag_sum = sum([arr[i][i] for i in range(n)])
    left_diag_sum = sum([arr[i][n - i - 1] for i in range(n)])
    maxval = max(maxval, right_diag_sum)
    maxval = max(maxval, left_diag_sum)

    return maxval


def main():
    sys.stdin = open("python-SWExpert/input.txt")

    T = 10
    for _ in range(1, T + 1):
        t = int(input())
        matrix = []
        for _ in range(100):
            matrix.append(list(map(int, input().split())))
        ans = solution(matrix)
        print("#{} {}".format(t, ans))


if __name__ == "__main__":
    main()
