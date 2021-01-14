"""
시간 : 50개 테스트케이스를 합쳐서 C의 경우 3초 / C++의 경우 3초 / Java의 경우 3초 / python의 경우 15초
메모리 : 힙, 정적 메모리 합쳐서 256MB 이내, 스택 메모리 1MB 이내

"""

import sys


def solution(N, room):
    # person과 stair 만들기
    persons, stairs = [], []
    for x in range(N):
        for y in range(N):
            if not room[x][y]:
                pass
            elif room[x][y] == 1:
                persons.append((x, y))
            else:
                stairs.append((x, y, room[x][y]))
    stairs.sort(key=lambda z: z[2])

    # stair 0번, 1번과 person까지의 거리 계산
    dist_0, dist_1 = [], []
    for px, py in persons:
        dist_0.append(abs(px - stairs[0][0]) + abs(py - stairs[0][1]))
        dist_1.append(abs(px - stairs[1][0]) + abs(py - stairs[1][1]))

    min_time = 10000
    for i in range(1 << len(persons)):
        # 0번 stair를 이용하는 경우와 1번 stair를 이용하는 경우 2^persons개
        p2s_0, p2s_1 = [], []
        for j in range(len(persons)):
            if i & (1 << j):
                p2s_0.append(dist_0[j])
            else:
                p2s_1.append(dist_1[j])
        # 각각 stair별로 계산하므로 계산하기 편하게 sort
        p2s_0.sort()
        p2s_1.sort()

        # 시간 계산
        stair_0, stair_1 = [0] * 3, [0] * 3
        for i, d_0 in enumerate(p2s_0):
            stair_0[i % 3] = max(d_0 + 1, stair_0[i % 3]) + stairs[0][2]
        for i, d_1 in enumerate(p2s_1):
            stair_1[i % 3] = max(d_1 + 1, stair_1[i % 3]) + stairs[1][2]
        # 가장 오래걸렸던 시간을 총 걸린 시간으로 assign
        taken_time = max(max(stair_0), max(stair_1))
        # 모든 경우 중 최소시간 비교 & 대입
        min_time = min(min_time, taken_time)
    return min_time


def main():
    sys.stdin = open("python-SWExpert\\input.txt", "r")

    T = int(input())
    for t in range(1, T + 1):
        N = int(input())
        room = []
        for _ in range(N):
            room.append(list(map(int, input().split())))
        ans = solution(N, room)
        print("#{} {}".format(t, ans))


if __name__ == "__main__":
    main()

# 1 9
# 2 8
# 3 9
# 4 7
# 5 8
# 6 8
# 7 11
# 8 11
# 9 18
# 10 12
