"""
시간 : 50개 테스트케이스를 합쳐서 C의 경우 3초 / C++의 경우 3초 / Java의 경우 3초 / python의 경우 15초
메모리 : 힙, 정적 메모리 합쳐서 256MB 이내, 스택 메모리 1MB 이내

"""

import sys


def solution(N, room):
    persons, stairs = [], []
    for x in range(N):
        for y in range(N):
            if not room[x][y]:
                pass
            elif room[x][y] == 1:
                persons.append((x, y))
            else:
                stairs.append((x, y))
    stairs.sort(key=lambda z: room[z[0]][z[1]])

    dist = [[0 for _ in range(len(persons))] for _ in range(len(stairs))]
    for pi, (px, py) in enumerate(persons):
        for si, (sx, sy) in enumerate(stairs):
            dist[si][pi] = abs(px - sx) + abs(py - sy)

    turn = 1
    persons_count, num_of_person = 0, len(persons)
    time_to_down = [room[sx][sy] for sx, sy in stairs]
    stairs_queue = [list() for _ in range(len(stairs))]
    moved = [False] * num_of_person

    while persons_count < num_of_person:
        for si, dist_info in enumerate(dist):
            while stairs_queue[si] and stairs_queue[si][0] <= turn:
                stairs_queue[si].pop(0)
            for pi, d in enumerate(dist_info):
                if len(stairs_queue[si]) == 3:
                    break
                if not moved[pi] and d < turn:
                    stairs_queue[si].append(turn + time_to_down[si])
                    moved[pi] = True
                    persons_count += 1
        turn += 1

    for turns in stairs_queue:
        for t in turns:
            turn = max(turn, t)
    return turn


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
