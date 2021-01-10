# https://swexpertacademy.com/main/solvingProblem/solvingProblem.do

"""
시간 : 50개 테스트케이스를 합쳐서 C의 경우 30초 / C++의 경우 30초 / Java의 경우 30초 / Python의 경우 30초
메모리 : 힙, 정적 메모리 합쳐서 256MB 이내, 스택 메모리 1MB 이내

"""

import sys


def check_valid(arr, x):
    preq = arr[0]
    count = 0
    airstrip = [False] * len(arr)
    need_airstrip = 0
    for i, num in enumerate(arr):
        if need_airstrip:
            if preq == num:
                need_airstrip -= 1
                airstrip[i] = True
            else:
                return False
        elif preq == num:
            count += 1
        elif preq + 1 == num:
            if count < x:
                return False
            for back in range(1, x + 1):
                if airstrip[i - back]:
                    return False
            count = 1
        elif preq - 1 == num:
            airstrip[i] = True
            need_airstrip = x - 1
            count = 1
        else:
            return False
        preq = num
    if need_airstrip:
        return False
    return True


def solution(N, X, rows):
    count = 0
    for i in range(N):
        count += int(check_valid(rows[i], X))
        count += int(check_valid([row[i] for row in rows], X))  # cols

    return count


def main():
    sys.stdin = open("python-SWExpert\input.txt", "r")

    T = int(input())
    for t in range(1, T + 1):
        matrix = []
        N, X = map(int, input().split())
        for _ in range(N):
            matrix.append(list(map(int, input().split())))
        ans = solution(N, X, matrix)
        print("#{} {}".format(t, ans))


if __name__ == "__main__":
    main()


"""
Sample Output
#1 7
#2 4
#3 11
#4 11
#5 15
#6 4
#7 4
#8 1
#9 5
#10 8
"""