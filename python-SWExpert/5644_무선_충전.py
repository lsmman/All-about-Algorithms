"""
시간 : 50개 테스트케이스를 합쳐서 C의 경우 3초 / C++의 경우 3초 / Java의 경우 3초 / python의 경우 15초
메모리 : 힙, 정적 메모리 합쳐서 256MB 이내, 스택 메모리 1MB 이내

"""
import sys


def move_point(point, move):
    return (point[0] + move[0], point[1] + move[1])


def solution(num_of_move, num_of_AP, user, AP):
    # AP : x, y, C, P
    # 1 up, 2 right, 3 down, 4 left
    direct = [(0, 0), (0, -1), (1, 0), (0, 1), (-1, 0)]
    AP_checker = [[0 for _ in range(11)] for __ in range(11)]

    for i in range(1, 11):
        for j in range(1, 11):
            for AP_idx, (x, y, C, _P) in enumerate(AP):
                if abs(i - x) + abs(j - y) <= C:
                    AP_checker[i][j] |= 1 << AP_idx

    A, B = (1, 1), (10, 10)
    sum_of_charge = 0
    for move_0, move_1 in zip(user[0] + [0], user[1] + [0]):
        can_conn_A, can_conn_B = [], []
        for i in range(num_of_AP):
            if AP_checker[A[0]][A[1]] & (1 << i):
                can_conn_A.append(i)
            if AP_checker[B[0]][B[1]] & (1 << i):
                can_conn_B.append(i)

        if not can_conn_A and not can_conn_B:
            pass
        elif not can_conn_A:
            sum_of_charge += max([AP[i][3] for i in can_conn_B])
        elif not can_conn_B:
            sum_of_charge += max([AP[i][3] for i in can_conn_A])
        else:
            cases = []
            charge_temp = 0
            for a in can_conn_A:
                for b in can_conn_B:
                    cases.append((a, b))
            for a, b in cases:
                if a == b:
                    charge_temp = max(charge_temp, AP[a][3])
                else:
                    charge_temp = max(charge_temp, AP[a][3] + AP[b][3])
            sum_of_charge += charge_temp

        A = move_point(A, direct[move_0])
        B = move_point(B, direct[move_1])

    return sum_of_charge


"""
BC1
Loca (4, 4)
Coverage 1 = 충전 범위
Performance 100 = 성능

두점 사이에 거리 abs(XA - XB) + abs(YA - YB)

"""


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
