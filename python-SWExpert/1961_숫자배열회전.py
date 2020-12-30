import sys


def solution(n, matrix):
    # 90 degree : x, y -> y, n-x-1
    # 180 degree : x, y ->-> n-x-1, n-y-1
    # 270 degree : x, y ->->-> n-y-1, x
    for x in range(n):
        a, b, c = "", "", ""
        for y in range(n):
            a += str(matrix[n - y - 1][x])
            b += str(matrix[n - x - 1][n - y - 1])
            c += str(matrix[y][n - x - 1])
        print(a, b, c)
    return


def main():
    sys.stdin = open("python-SWExpert/input.txt")

    T = int(input())
    for test_case in range(1, T + 1):
        n = int(input())
        matrix = []
        for _ in range(n):
            matrix.append(list(map(int, input().split())))
        print("#{}".format(test_case))
        solution(n, matrix)


if __name__ == "__main__":
    main()
