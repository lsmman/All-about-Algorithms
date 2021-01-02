import sys


def solution(r, c, commend):
    return 0


def main():
    sys.stdin = open("python-SWExpert/input.txt")

    T = int(input())
    for test_case in range(1, T + 1):
        r, c = map(int, input().split())
        commend = []
        for _ in range(r):
            commend.append(input())
        ans = solution(r, c, commend)
        print("#{} {}".format(test_case, ans))
        break


if __name__ == "__main__":
    main()
